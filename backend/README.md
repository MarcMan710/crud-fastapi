# Backend API (FastAPI)

This directory contains the FastAPI backend for the Product Management application. It provides a RESTful API to manage product data, including creation, retrieval, updating, and deletion operations.

## Features

- **GET /products**: Retrieve a list of all products.
- **GET /products/{id}**: Retrieve details of a specific product by ID.
- **POST /products**: Add a new product.
- **PUT /products/{id}**: Update an existing product by ID.
- **DELETE /products/{id}**: Delete a product by ID.

## Technologies Used

- FastAPI: Web framework for building APIs with Python.
- SQLAlchemy: SQL toolkit and Object-Relational Mapper (ORM) for interacting with the database.
- MySQL: Relational database to store product data.
- Uvicorn: ASGI server to run the FastAPI application.
- Pydantic: Data validation and settings management.

## Setup and Installation

Follow these steps to set up and run the backend API:

### 1. Database Setup (MySQL)

Before running the application, ensure you have a MySQL server running and create a database. By default, the application expects a database named `product_db`.

If your MySQL credentials or database name are different, you will need to update the connection string in `backend/app/database.py`:

```python
# backend/app/database.py
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://user:password@host/dbname"
```

Replace `user`, `password`, `host`, and `dbname` with your actual MySQL credentials and database name.

### 2. Install Dependencies

Navigate to the root of your project (`crud-fastapi`) and install the required Python packages using pip:

```bash
pip install fastapi uvicorn sqlalchemy mysql-connector-python pydantic
```

### 3. Run the Application

Navigate to the `backend` directory:

```bash
cd backend
```

Then, run the FastAPI application using Uvicorn:

```bash
uvicorn app.main:app --reload
```

The `--reload` flag enables auto-reloading, so the server will restart automatically when you make changes to the code.

The API will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

- **GET `/products`**
    - Returns a list of all products.
- **GET `/products/{id}`**
    - Retrieves product details by ID.
- **POST `/products`**
    - Adds a new product.
    - Request Body (JSON):
        ```json
        {
            "name": "string",
            "price": 0.0,
            "quantity": 0
        }
        ```
- **PUT `/products/{id}`**
    - Updates product data by ID.
    - Request Body (JSON):
        ```json
        {
            "name": "string",
            "price": 0.0,
            "quantity": 0
        }
        ```
- **DELETE `/products/{id}`**
    - Deletes a product by ID.

## Error Handling

The API includes basic error handling. For example, if a product is not found, a `404 Not Found` error will be returned. 