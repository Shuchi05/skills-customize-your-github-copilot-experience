import os
import sqlite3
from sqlite3 import Connection

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

DATABASE = "items.db"
app = FastAPI()

class ItemBase(BaseModel):
    name: str = Field(..., min_length=1)
    description: str | None = None
    price: float = Field(..., gt=0)

class Item(ItemBase):
    id: int


def get_db() -> Connection:
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    if not os.path.exists(DATABASE):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL
            )
            """
        )
        conn.commit()
        conn.close()


@app.on_event("startup")
def startup_event() -> None:
    init_db()


@app.get("/items")
def read_items(name: str | None = Query(None, description="Filter items by name")):
    conn = get_db()
    cursor = conn.cursor()
    if name:
        cursor.execute("SELECT * FROM items WHERE name LIKE ?", (f"%{name}%",))
    else:
        cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()
    conn.close()
    return [Item(**row) for row in rows]


@app.get("/items/{item_id}")
def read_item(item_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(**row)


@app.post("/items")
def create_item(item: ItemBase):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (name, description, price) VALUES (?, ?, ?)",
        (item.name, item.description, item.price),
    )
    conn.commit()
    item_id = cursor.lastrowid
    conn.close()
    return Item(id=item_id, **item.dict())


@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemBase):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE items SET name = ?, description = ?, price = ? WHERE id = ?",
        (item.name, item.description, item.price, item_id),
    )
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")
    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    row = cursor.fetchone()
    conn.close()
    return Item(**row)


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    row = cursor.fetchone()
    if row is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")
    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    return {"detail": "Item deleted"}


# Example request body for POST /items:
# {
#   "name": "Notebook",
#   "description": "A spiral notebook for notes",
#   "price": 4.99
# }
