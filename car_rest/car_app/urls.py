from django.urls import path

from . import views

urlpatterns = [
    path('list', views.car_list, name='car_list'),
    path("<int:pk>", views.car_detail, name='car_detail'),
    path("showroom",views.show_rooms.as_view(), name='showroom'),
    path("showroom/<int:pk>", views.showRoom_details.as_view(), name='showroom_details'),
]