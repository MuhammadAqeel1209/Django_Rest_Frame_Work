# # from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view,authentication_classes
from rest_framework.response import Response
from user_app.api.serialization import UserRegistration
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

# Token Authencation 
@api_view(['POST'])
def userRegister(request):
    if request.method == 'POST':
        serializer = UserRegistration(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def userLogOut(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    
    



# JWT Authencation 
# @api_view(['POST'])
# def userRegister(request):
#     """
#     Handle user registration.
#     """
#     if request.method == 'POST':
#         serializer = UserRegistration(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             # Generate JWT tokens for the new user
#             # refresh = RefreshToken.for_user(user)
#             # data = {
#             #     'user': serializer.data,
#             #     'refresh': str(refresh),
#             #     'access': str(refre .access_token),
#             # }
            
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def userLogOut(request):
#     """
#     Handle user logout by blacklisting the refresh token.
#     """
#     if request.method == 'POST':
#         try:
#             # refresh_token = request.data.get("refresh")
#             # if refresh_token is None:
#             #     return Response(
#             #         {"error": "Refresh token is required."}, 
#             #         status=status.HTTP_400_BAD_REQUEST
#             #     )
#             # token = RefreshToken(refresh_token)
#             # token.blacklist()
#             return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
