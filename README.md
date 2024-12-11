# Django Rest Framework - Car Management API

This is a Django Rest Framework (DRF) project that provides an API to manage a list of cars. The API allows you to view all cars or fetch details of a specific car using its primary key.

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Virtual Environment (optional but recommended)
- Django and Django Rest Framework (DRF)

---

## Installation

### 1. Clone the Repository
```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Set Up Virtual Environment
Create a virtual environment and activate it:
```bash
python -m venv django_rest
django_rest\Scripts\activate
```
(For macOS/Linux, use `source django_rest/bin/activate` to activate the virtual environment.)

### 3. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

---

## Running the Application

1. Navigate to the project folder:
    ```bash
    cd car_rest
    ```

2. Run the server:
    ```bash
    python manage.py runserver
    ```

3. Access the API in your browser:
    - List all cars: [http://127.0.0.1:8000/car/list](http://127.0.0.1:8000/car/list)
    - View a specific car (replace `{primary_key}` with the ID of the car):  
      [http://127.0.0.1:8000/car/{primary_key}](http://127.0.0.1:8000/car/{primary_key})

---

## API Endpoints

- **GET /car/list**  
  Retrieves a list of all cars.

- **GET /car/{primary_key}**  
  Retrieves details of a specific car by its primary key.

---

## Development

### Adding New Features
1. Create a new Django app:
    ```bash
    python manage.py startapp <app_name>
    ```

2. Add the app to the `INSTALLED_APPS` in `settings.py`.

3. Use DRF's serializers, views, and routers to define new API endpoints.

### Example of Adding a Serializer:
```python
from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
```

---

## Using Django Rest Framework (DRF)

### Key Features of DRF Used in This Project:
- **Serializers**: Convert querysets and model instances into JSON and vice versa.
- **Generic Views**: Simplify creating CRUD operations.
- **URL Routers**: Automatically generate URLs for API endpoints.
- **Browsable API**: A web interface for interacting with the API.

### DRF Installation
If Django Rest Framework is not already installed, you can install it using pip:
```bash
pip install djangorestframework
```

Add `'rest_framework'` to the `INSTALLED_APPS` in `settings.py`:
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

---

## Contributing

Feel free to fork the repository and create a pull request for any new features or bug fixes.

---
