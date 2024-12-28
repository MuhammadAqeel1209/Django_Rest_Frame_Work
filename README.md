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

To add `ModelViewSet` for your project, we will use Django Rest Framework's `ModelViewSet`, which combines the functionality of `ViewSet` and generic views. Here's how you can implement it for both `CarList` and `ShowRoom` models.

---

### **1. Update `views.py` with `ModelViewSet`**

#### `views.py`
```python
from rest_framework import viewsets
from .models import CarList, ShowRoom
from .serializers import CarSerializer, ShowroomSerializer

class CarModelViewSet(viewsets.ModelViewSet):
    """
    A ModelViewSet for managing CarList objects.
    Provides CRUD operations.
    """
    queryset = CarList.objects.all()
    serializer_class = CarSerializer

class ShowRoomModelViewSet(viewsets.ModelViewSet):
    """
    A ModelViewSet for managing ShowRoom objects.
    Provides CRUD operations.
    """
    queryset = ShowRoom.objects.all()
    serializer_class = ShowroomSerializer
```

---

### **2. Register `ModelViewSet` with Router**

Update your `urls.py` to register the new `ModelViewSet` classes using `DefaultRouter`.

#### `urls.py`
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarModelViewSet, ShowRoomModelViewSet

# Initialize the router
router = DefaultRouter()

# Register ModelViewSets with the router
router.register(r'cars', CarModelViewSet, basename='car')
router.register(r'showrooms', ShowRoomModelViewSet, basename='showroom')

# URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include routes managed by the router
]
```

---

### **3. Benefits of `ModelViewSet`**

Using `ModelViewSet` will automatically provide these endpoints:

#### Cars Endpoints:
- `GET /cars/` - List all cars
- `POST /cars/` - Create a new car
- `GET /cars/{id}/` - Retrieve a car by ID
- `PUT /cars/{id}/` - Update a car by ID
- `PATCH /cars/{id}/` - Partially update a car
- `DELETE /cars/{id}/` - Delete a car

#### Showrooms Endpoints:
- `GET /showrooms/` - List all showrooms
- `POST /showrooms/` - Create a new showroom
- `GET /showrooms/{id}/` - Retrieve a showroom by ID
- `PUT /showrooms/{id}/` - Update a showroom by ID
- `PATCH /showrooms/{id}/` - Partially update a showroom
- `DELETE /showrooms/{id}/` - Delete a showroom

---

### **4. Testing the Endpoints**

1. Run the development server:
   ```bash
   python manage.py runserver
   ```
2. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the API root.
3. Use tools like **Postman**, **cURL**, or the DRF web interface to test the endpoints.

### **Custom Permissions in Django Rest Framework (DRF)**

Custom permissions in Django Rest Framework (DRF) provide fine-grained control over API access. They allow developers to define specific rules for who can perform certain actions, beyond the default permission classes provided by DRF.

---

### **How Custom Permissions Work**

Custom permissions are implemented by subclassing `BasePermission` from `rest_framework.permissions`. A custom permission class typically overrides one or both of these methods:

1. **`has_permission(self, request, view)`**  
   This method checks if the user has general access to a view. It’s called once per request, before any view-specific object-level checks.

2. **`has_object_permission(self, request, view, obj)`**  
   This method checks permissions for a specific object. It’s called during requests that act on a single object, like `GET`, `PUT`, or `DELETE` for a specific resource.

---

### **Example: Custom Permission**

#### **IsAdminOrReadOnly**
This permission allows read-only access for everyone but restricts write operations to admin users.

```python
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to allow only admins to edit objects.
    Others can only read the data.
    """

    def has_permission(self, request, view):
        # SAFE_METHODS includes GET, HEAD, and OPTIONS
        if request.method in SAFE_METHODS:
            return True  # Allow read-only access for all users

        # Write permissions are only allowed for admin users
        return request.user and request.user.is_staff
```

---

### **How to Use Custom Permissions**

1. Define the custom permission class in your project.
2. Attach the custom permission to a view or a viewset by setting the `permission_classes` attribute.

#### Example Usage:
```python
from rest_framework.viewsets import ModelViewSet
from .models import CarList
from .serializers import CarSerializer
from .permissions import IsAdminOrReadOnly

class CarModelViewSet(ModelViewSet):
    """
    A ModelViewSet for managing CarList objects with custom permissions.
    """
    queryset = CarList.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAdminOrReadOnly]
```

---

### **When to Use Custom Permissions**

- **Read-Only APIs for Public Users:** Allow unrestricted access to view data but limit modifications to authenticated or privileged users.
- **Role-Based Access Control (RBAC):** Differentiate permissions based on user roles (e.g., admin, editor, viewer).
- **Object-Level Restrictions:** Control access to specific objects, such as ensuring users can only edit their own data.

---

### **Advantages of Custom Permissions**

- **Granularity:** Fine-tuned control over API access.
- **Reusability:** Once defined, custom permissions can be reused across multiple views or viewsets.
- **Security:** Ensures sensitive operations are restricted to authorized users.

By implementing custom permissions, you can make your API secure, robust, and tailored to specific access requirements.

### **Token Authentication in Django Rest Framework (DRF)**

Token-based authentication is a mechanism for securing APIs in Django Rest Framework (DRF). It uses tokens to validate the identity of users. A token is a unique string generated for a user upon successful login, which is sent with subsequent requests to authenticate the user.

---

### **How Token Authentication Works**

1. **User Authentication**: The user provides valid credentials (e.g., username and password).
2. **Token Generation**: Upon successful login, the server generates a token and sends it to the client.
3. **Token Usage**: The client includes the token in the `Authorization` header of subsequent API requests.
4. **Token Validation**: The server validates the token and identifies the user.

---

### **Setup Token Authentication in DRF**

#### **1. Install DRF If Not Installed**
Ensure that Django Rest Framework is installed in your environment:
```bash
pip install djangorestframework
```

#### **2. Add DRF to Installed Apps**
Include `'rest_framework'` and `'rest_framework.authtoken'` in your `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'rest_framework.authtoken',
]
```

#### **3. Migrate Database**
Run migrations to create the necessary database table for storing tokens:
```bash
python manage.py migrate
```

#### **4. Generate Tokens for Users**
You can create tokens manually for users or generate them programmatically:
```bash
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Generate a token for an existing user
user = User.objects.get(username='username')
token, created = Token.objects.get_or_create(user=user)
print(token.key)  # Print the token key
```

---

### **5. Update Settings for Token Authentication**
Configure DRF to use token authentication in your `settings.py` file:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

---

### **6. Create a Token Authentication Endpoint**

To allow users to obtain tokens via an API, use the built-in `obtain_auth_token` view:

#### **urls.py**
```python
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
```

---

### **7. Usage in API Requests**

Clients must include the token in the `Authorization` header of each API request:

#### Example:
```http
GET /api/cars/ HTTP/1.1
Host: example.com
Authorization: Token <your_token_here>
```

---

### **8. Protecting API Endpoints**

Apply `IsAuthenticated` or other permissions to secure endpoints:

#### Example View:
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You are authenticated!"})
```

---

### **Testing Token Authentication**

1. **Obtain a Token**: Use the `/api/token/` endpoint with valid credentials to get a token.
2. **Use the Token**: Include the token in the `Authorization` header of subsequent API requests.
3. **Test Secure Endpoints**: Verify that endpoints protected with `IsAuthenticated` are accessible only with a valid token.

---

### **Advantages of Token Authentication**

1. **Stateless**: No session data is stored on the server, making it scalable.
2. **Reusability**: The same token can be reused for multiple requests.
3. **Decoupled Frontend**: Works seamlessly with SPAs and mobile apps.

---

### **Considerations**

- **Token Expiry**: Tokens do not expire by default. Consider using packages like `django-rest-framework-simplejwt` if you need expiration and refresh functionality.
- **Secure Storage**: Tokens should be stored securely on the client side (e.g., HTTP-only cookies or secure storage).
- **HTTPS**: Always use HTTPS to prevent token interception.
To implement token authentication for user registration, login, and logout in your Django Rest Framework (DRF) project, you can follow these steps and update the `README.md` file accordingly.

---

### **Token Authentication for User Registration, Login, and Logout**

To enable token authentication for user registration, login, and logout, follow these steps:

---

### **1. Install the Required Package**

Make sure that you have `djangorestframework` and `djangorestframework.authtoken` installed:

```bash
pip install djangorestframework
pip install djangorestframework.authtoken
```

---

### **2. Update `INSTALLED_APPS` in `settings.py`**

Add `'rest_framework'` and `'rest_framework.authtoken'` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'rest_framework.authtoken',
]
```

---

### **3. Migrate the Database**

Run the migrations to create necessary tables for token authentication:

```bash
python manage.py migrate
```

---

### **4. Create the User Registration and Login Views**

Create views for user registration and login in `views.py`:

#### **`views.py`**
```python
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def register_user(request):
    """
    Register a new user and generate a token.
    """
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login_user(request):
    """
    Login an existing user and return a token.
    """
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout_user(request):
    """
    Logout a user by deleting their token.
    """
    if request.method == 'POST' and request.user.is_authenticated:
        request.user.auth_token.delete()
        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
    return Response({"error": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)
```

---

### **5. Add the URLs for Registration, Login, and Logout**

Update your `urls.py` to include endpoints for user registration, login, and logout:

#### **`urls.py`**
```python
from django.urls import path
from .views import register_user, login_user, logout_user

urlpatterns = [
    path('api/register/', register_user, name='register'),
    path('api/login/', login_user, name='login'),
    path('api/logout/', logout_user, name='logout'),
]
```

---

### **6. Configure Token Authentication in `settings.py`**

Update your `settings.py` to enable token authentication:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

---

### **7. Test the Endpoints**

- **Register**: `POST /api/register/` with the fields `username`, `password`, and `email`.
- **Login**: `POST /api/login/` with the fields `username` and `password`.
- **Logout**: `POST /api/logout/` with the authorization token in the `Authorization` header.

---

### **8. Example Request and Response**

#### **Register User**

**Request**:

```bash
POST /api/register/
Content-Type: application/json

{
    "username": "john_doe",
    "password": "password123",
    "email": "john@example.com"
}
```

**Response**:

```json
{
    "token": "abc123xyz"
}
```

---

#### **Login User**

**Request**:

```bash
POST /api/login/
Content-Type: application/json

{
    "username": "john_doe",
    "password": "password123"
}
```

**Response**:

```json
{
    "token": "abc123xyz"
}
```

---

#### **Logout User**

**Request**:

```bash
POST /api/logout/
Authorization: Token abc123xyz
```

**Response**:

```json
{
    "message": "Successfully logged out."
}
```
# Django Rest Framework (DRF) Car Management API

This project demonstrates how to build a Car Management API using Django Rest Framework (DRF). Below are the steps and details for implementing the API.

## Features
- CRUD operations for car details
- Token-based authentication
- JWT (JSON Web Token) authentication

---

## Prerequisites

Make sure you have the following installed:
- Python 3.8+
- Django 4.0+
- Django Rest Framework
- djangorestframework-simplejwt (for JWT authentication)

Install the required dependencies:

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

---

## Project Setup

### 1. Create a Django Project

```bash
django-admin startproject car_management
cd car_management
python manage.py startapp cars
```

### 2. Add the App to Installed Apps

In `settings.py`, add `'cars'` and `'rest_framework'` to `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
    'cars',
]
```

### 3. Update the REST Framework Settings

Add the following to `settings.py` to enable JWT authentication:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
```

---

## Models

In `cars/models.py`, define the `Car` model:

```python
from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.brand} {self.name} ({self.year})"
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Serializers

In `cars/serializers.py`, create a serializer for the `Car` model:

```python
from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
```

---

## Views

In `cars/views.py`, create views for CRUD operations:

```python
from rest_framework import generics
from .models import Car
from .serializers import CarSerializer

class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
```

---

## URLs

In `cars/urls.py`, define routes for the views:

```python
from django.urls import path
from .views import CarListCreateView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('cars/', CarListCreateView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarRetrieveUpdateDestroyView.as_view(), name='car-detail'),
]
```

Include these URLs in the project `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cars.urls')),
]
```

---

## Permissions

To apply permissions, update `cars/views.py`:

```python
from rest_framework.permissions import IsAuthenticated

class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

class CarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]
```

---

## JWT Authentication

### 1. Configure JWT Routes

In the project `urls.py`, add JWT routes:

```python
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

### 2. Obtain Tokens

- To get a token, send a POST request to `/api/token/` with valid user credentials.

Example request:

```bash
POST /api/token/
{
    "username": "your_username",
    "password": "your_password"
}
```

- Refresh tokens using `/api/token/refresh/`:

```bash
POST /api/token/refresh/
{
    "refresh": "your_refresh_token"
}
```

### 3. Use Tokens in Requests

Include the access token in the `Authorization` header for protected routes:

```bash
Authorization: Bearer your_access_token
```

---

## Testing

Use tools like Postman or cURL to test the API endpoints. Ensure the following:
1. JWT authentication is required for protected routes.
2. CRUD operations work as expected.
3. Tokens are refreshed successfully.

---

## Conclusion

This project provides a simple yet robust foundation for building APIs using Django Rest Framework and JWT authentication.


---
