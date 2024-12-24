To integrate `ViewSet` and `Router` into the provided Django Rest Framework (DRF) project, here's how you can update your implementation. The `ViewSet` simplifies CRUD operations for your models, and the `Router` handles automatic URL routing.

---

### **Adding ViewSet for Cars and Showrooms**

In the `views.py`, create `ViewSet` classes for `CarList` and `ShowRoom` models.

#### `views.py`
```python
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CarList, ShowRoom
from .serializers import CarSerializer, ShowroomSerializer

class CarViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for managing car objects.
    """
    queryset = CarList.objects.all()
    serializer_class = CarSerializer

class ShowRoomViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for managing showroom objects.
    """
    queryset = ShowRoom.objects.all()
    serializer_class = ShowroomSerializer
```

---

### **Registering ViewSets with Router**

Update your `urls.py` file to register the `CarViewSet` and `ShowRoomViewSet` with the `DefaultRouter`. This will automatically generate RESTful API routes for the models.

#### `urls.py`
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, ShowRoomViewSet

# Initialize the router
router = DefaultRouter()

# Register the ViewSets
router.register(r'cars', CarViewSet, basename='car')
router.register(r'showrooms', ShowRoomViewSet, basename='showroom')

# URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include all routes from the router
]
```

---

### **Generated API Endpoints**

The router automatically generates the following endpoints:

#### Cars Endpoints
- **List Cars**: `GET /cars/`
- **Create Car**: `POST /cars/`
- **Retrieve Car**: `GET /cars/{id}/`
- **Update Car**: `PUT /cars/{id}/`
- **Partial Update Car**: `PATCH /cars/{id}/`
- **Delete Car**: `DELETE /cars/{id}/`

#### Showrooms Endpoints
- **List Showrooms**: `GET /showrooms/`
- **Create Showroom**: `POST /showrooms/`
- **Retrieve Showroom**: `GET /showrooms/{id}/`
- **Update Showroom**: `PUT /showrooms/{id}/`
- **Partial Update Showroom**: `PATCH /showrooms/{id}/`
- **Delete Showroom**: `DELETE /showrooms/{id}/`

---

### **Testing the API**
1. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
2. Access the API root at [http://127.0.0.1:8000/](http://127.0.0.1:8000/). You should see the endpoints for `cars` and `showrooms`.

---