from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.view import userRegister,userLogOut

urlpatterns = [
    path('login/',obtain_auth_token,name='login'),
    path('register/',userRegister,name='register'),
    path('logout/',userLogOut,name='logout'),
]
