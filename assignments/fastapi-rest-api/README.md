# 📘 Assignment: FastAPI REST API

## 🎯 Objective

Learn how to build a RESTful web API using FastAPI by defining endpoints, handling requests, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create CRUD Endpoints

#### Description
Build a FastAPI app that exposes CRUD endpoints for managing a simple list of items.

#### Requirements
Completed program should:

- Use FastAPI to define an application instance.
- Create endpoints to:
  - list all items (`GET /items`)
  - retrieve a single item by ID (`GET /items/{item_id}`)
  - add a new item (`POST /items`)
  - update an existing item (`PUT /items/{item_id}`)
  - delete an item (`DELETE /items/{item_id}`)
- Return JSON responses with appropriate status codes.
- Use a simple in-memory list or dictionary to store items.

### 🛠️ Add Validation and Error Handling

#### Description
Enhance the API with input validation, data models, and user-friendly error responses.

#### Requirements
Completed program should:

- Define a Pydantic model for the item schema.
- Validate incoming request data for `POST` and `PUT` endpoints.
- Return a `404 Not Found` response when an item ID does not exist.
- Return a `400 Bad Request` response for invalid input.
- Include example JSON request bodies in comments or documentation.
