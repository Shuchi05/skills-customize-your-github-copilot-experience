# 📘 Assignment: FastAPI SQLite REST API

## 🎯 Objective

Build a persistent REST API using FastAPI and SQLite so students learn how to store and manage data across requests.

## 📝 Tasks

### 🛠️ Implement persistent CRUD endpoints

#### Description
Create a FastAPI application that stores items in a SQLite database and provides full CRUD support.

#### Requirements
Completed program should:

- Initialize a SQLite database and create a table for items.
- Provide endpoints to:
  - list all items (`GET /items`)
  - retrieve a single item by ID (`GET /items/{item_id}`)
  - add a new item (`POST /items`)
  - update an item (`PUT /items/{item_id}`)
  - delete an item (`DELETE /items/{item_id}`)
- Use JSON responses for all endpoints.
- Return `404 Not Found` when an item ID does not exist.

### 🛠️ Add validation and search support

#### Description
Enhance the API with request validation and a simple search or filter endpoint.

#### Requirements
Completed program should:

- Define Pydantic models for item creation and response data.
- Validate input for `POST` and `PUT` requests.
- Reject invalid payloads with a `400 Bad Request` response.
- Provide a query parameter for filtering items by name, for example `GET /items?name=book`.
- Include example request body JSON in comments or documentation.
