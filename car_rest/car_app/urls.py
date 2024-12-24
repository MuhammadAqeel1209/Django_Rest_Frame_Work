from django.urls import path,include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'showroom',views.ShowRoom_viewSet,basename='showroom')

urlpatterns = [
    path('list', views.car_list, name='car_list'),
    path("<int:pk>", views.car_detail, name='car_detail'),
    path('', include(router.urls)),

    # path("showroom",views.show_rooms.as_view(), name='showroom'),
    # path("showroom/<int:pk>", views.showRoom_details.as_view(), name='showroom_details'),
    path('reiview',views.ReiviewList.as_view(), name='reiview'),
    path('reiview/<int:pk>',views.ReiviewDetail.as_view(), name='reiviewDetail'),
]