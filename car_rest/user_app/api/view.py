from rest_framework.decorators import api_view,authentication_classes
from rest_framework.response import Response
from user_app.api.serialization import UserRegistration
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

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
