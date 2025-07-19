# Frontend (Flask)

This directory contains the Flask frontend for the Product Management application. It provides a simple HTML-based user interface to interact with the FastAPI backend API for managing product data.

## Features

- **Display Products**: View a list of all products.
- **Add Product**: Add new product data through a form.
- **Edit Product**: Update existing product details using a form.
- **Delete Product**: Remove products from the list.

## Technologies Used

- Flask: A micro web framework for Python.
- `requests`: A Python library for making HTTP requests to the backend API.
- HTML/CSS: For structuring and styling the user interface.

## Setup and Installation

Follow these steps to set up and run the Flask frontend:

### 1. Install Dependencies

Navigate to the root of your project (`crud-fastapi`) and install the required Python packages using pip:

```bash
pip install flask requests
```

### 2. Run the Application

Ensure your FastAPI backend is running first. You can refer to the `backend/README.md` for instructions on how to start the backend API.

Once the backend is running, navigate to the `frontend` directory:

```bash
cd frontend
```

Then, run the Flask application:

```bash
python app.py
```

The frontend application will be accessible at `http://127.0.0.1:5000`.

## Integration with Backend

The Flask frontend communicates with the FastAPI backend through HTTP requests. The base URL for the backend API is configured in `frontend/app.py`:

```python
# frontend/app.py
FASTAPI_BASE_URL = "http://127.0.0.1:8000"
```

Ensure that this URL matches the address where your FastAPI backend is running. 