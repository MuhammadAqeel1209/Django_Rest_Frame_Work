---

# Django Rest Framework - Car Management API

This is a Django Rest Framework (DRF) project that provides an API to manage a list of cars. The API allows you to view, add, update, or delete car details.

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

### 4. Run Migrations
Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
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
    - Add a new car: [http://127.0.0.1:8000/car/list](http://127.0.0.1:8000/car/list) (POST)
    - View, update, or delete a specific car (replace `{primary_key}` with the ID of the car):
      [http://127.0.0.1:8000/car/{primary_key}](http://127.0.0.1:8000/car/{primary_key})

---

## Models

### Car Model
- **File**: [`models.py`](#models)  
- **Key Features**: Represents individual cars, including name, description, price, and unique car number.

### Showroom Model
- **File**: [`models.py`](#models)  
- **Key Features**: Represents a showroom with multiple cars in its collection.

---

## Serializers

- **File**: [`serializers.py`](#serializers)
- **Custom Serializer**: The `CarSerializer` includes a dynamically computed field:
  - **`discount_price`**: Calculates the discounted price dynamically in API responses.
  - **Validation**: Includes custom validation for fields like price, car name, and car description.

### Nested Serializer Example
To link cars to showrooms, you can use a nested serializer:

```python
from rest_framework import serializers
from .models import CarList, ShowRoom

class CarSerializer(serializers.ModelSerializer):
    discount_price = serializers.SerializerMethodField()

    class Meta:
        model = CarList
        fields = "__all__"

    def get_discount_price(self, obj):
        return obj.price - 5000  # Apply a discount of 5000

    def validate_price(self, value):
        if value <= 20000.00:
            raise serializers.ValidationError("Price must be more than 20,000.")
        return value

    def validate(self, data):
        if data["car_name"] == data["car_decstr"]:
            raise serializers.ValidationError("Car name and description cannot be the same.")
        return data

class ShowroomSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True)

    class Meta:
        model = ShowRoom
        fields = "__all__"
```

For more details on the `ShowroomSerializer` with nested `CarSerializer`, refer to the **Custom Serializer** section in [`serializers.py`](#serializers).

---

## Class-Based Views (CBVs)

- **File**: [`views.py`](#views)  
- **Overview**: The project uses Django Rest Framework’s Class-Based Views (CBVs) to handle CRUD operations for cars and showrooms.

### Key Views:
1. **CarListView**: For listing and creating cars.
2. **CarDetailView**: For retrieving, updating, and deleting cars.
3. **ShowroomListView**: For listing and creating showrooms.
4. **ShowroomDetailView**: For retrieving, updating, and deleting showrooms.

Directly access the detailed implementation in the [`views.py`](#views) file.

---

## Mixins and Generic Views

The project leverages Django Rest Framework's **mixins** and **generic views** to simplify code for common operations:

### Mixins
- `CreateModelMixin`: Provides a method for creating new instances.
- `RetrieveModelMixin`: Provides a method for retrieving specific instances.
- `UpdateModelMixin`: Provides a method for updating existing instances.
- `DestroyModelMixin`: Provides a method for deleting instances.

For more information, see the [Using Mixins](https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-mixins) section of the DRF documentation.

### Generic Views
- `ListCreateAPIView`: Combines listing and creating resources.
- `RetrieveUpdateDestroyAPIView`: Combines retrieval, updating, and deletion operations.

For more information, see the [Generic Views](https://www.django-rest-framework.org/api-guide/generic-views/) section of the DRF documentation.

**Example Implementation**:

```python
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import CarList
from .serializers import CarSerializer

class CarListView(ListCreateAPIView):
    queryset = CarList.objects.all()
    serializer_class = CarSerializer

class CarDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CarList.objects.all()
    serializer_class = CarSerializer
```

These views reduce boilerplate code and make API endpoints more maintainable.

---

## Concrete View Classes

Django Rest Framework provides **Concrete View Classes** to handle standard CRUD operations, further simplifying API development. These include:

- **`CreateAPIView`**: For creating objects.
- **`ListAPIView`**: For listing objects.
- **`RetrieveAPIView`**: For retrieving a specific object.
- **`DestroyAPIView`**: For deleting objects.
- **`UpdateAPIView`**: For updating objects.

### Example Usage

```python
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import CarList
from .serializers import CarSerializer

class CarCreateView(CreateAPIView):
    queryset = CarList.objects.all()
    serializer_class = CarSerializer

class CarListView(ListAPIView):
    queryset = CarList.objects.all()
    serializer_class = CarSerializer
```

These concrete classes allow for fine-grained control and minimal configuration for specific tasks.

---

## API Endpoints

- **Cars**:
  - [List/Create Cars](http://127.0.0.1:8000/car/list)
  - [Retrieve/Update/Delete Car](http://127.0.0.1:8000/car/{pk})

- **Showrooms**:
  - [List/Create Showrooms](http://127.0.0.1:8000/car/showroom)
  - [Retrieve/Update/Delete Showroom](http://127.0.0.1:8000/car/showroom/{pk})

- **Reviews**:
  - [List/Create Reviews](http://127.0.0.1:8000/car/reiview)
  - [Retrieve/Update/Delete Review](http://127.0.0.1:8000/car/reiview/{pk})

---

## Explore More

### Learn More about DRF Concepts:
- [Class-Based Views Documentation](https://www.django-rest-framework.org/api-guide/generic-views/)
- [Custom Serializers Documentation](https://www.django-rest-framework.org/api-guide/serializers/#serializer-fields)
- [Relationships in Django](https://docs.djangoproject.com/en/5.1/topics/db/examples/)
- [Serializer Relationships](https://www.django-rest-framework.org/api-guide/relations/)

---

## Difference Between Authentication and Permission

In Django Rest Framework (DRF), **authentication** and **permissions** serve distinct purposes in securing an API:

| **Aspect**         | **Authentication**                                               | **Permission**                                                 |
|---------------------|------------------------------------------------------------------|----------------------------------------------------------------|
| **Purpose**         | Confirms the identity of the user making the request.           | Determines what the authenticated user is allowed to do.      |
| **Scope**           | Deals with **who** is making the request (e.g., user login).    | Deals with **what** the user is allowed to access or modify.  |
| **Implemented By**  | **Authentication classes** in DRF (`settings.py > DEFAULT_AUTHENTICATION_CLASSES`). | **Permission classes** in DRF (`settings.py > DEFAULT_PERMISSION_CLASSES`). |
| **Examples**        | Token-based, Session-based, or JWT-based authentication.        | Role-based access, object-level permissions, or custom rules. |
| **Configuration**   | Used to enforce user login or session validation.               | Used to restrict access to specific views or actions.         |
| **Key Methods**     | `authenticate(self, request)` in custom authentication classes. | `has_permission(self, request, view)` and `has_object_permission(self, request, view, obj)` in permission classes. |


