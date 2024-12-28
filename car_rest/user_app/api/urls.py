from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.view import userRegister,userLogOut
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


urlpatterns = [
    path('login/',obtain_auth_token,name='login'),
    path('register/',userRegister,name='register'),
    path('logout/',userLogOut,name='logout'),
    
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
