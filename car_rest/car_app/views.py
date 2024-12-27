from django.shortcuts import get_object_or_404
from .models import CarList, ShowRoom, Reivew

# from django.http import JsonResponse,HttpResponse
# import json
from .api_file.serialization import CarSerializer, ShowroomSerializer, ReiviewSerializer
from .api_file.permissions import ReiviewReadUsers,PermissionForAdmin
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.exceptions import ValidationError
from rest_framework.authentication import TokenAuthentication
# from rest_framework.authentication import BasicAuthentication,SessionAuthentication
# from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,DjangoModelPermissions
from rest_framework import viewsets

# ConcreteViewClasses
class ReiviewCreate(generics.CreateAPIView):
    serializer_class = ReiviewSerializer
    
    def get_queryset(self):
        return Reivew.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        car = get_object_or_404(CarList, pk=pk)
        user = self.request.user
        review_queryset = Reivew.objects.filter(car=car, apiUser=user)
        if review_queryset.exists():
            raise ValidationError('You have already provided a review for this car.')
        serializer.save(car=car, apiUser=user)

class ReiviewList(generics.ListAPIView):
    # queryset = Reivew.objects.all()
    serializer_class = ReiviewSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [PermissionForAdmin]
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Reivew.objects.filter(car=pk)
    
class ReiviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reivew.objects.all()
    serializer_class = ReiviewSerializer
    permission_classes = [ReiviewReadUsers]
    authentication_classes = [TokenAuthentication]


# Model ViewSet 
class ShowRoom_viewSet(viewsets.ModelViewSet):
    queryset = ShowRoom.objects.all()
    serializer_class = ShowroomSerializer


# # ViewSet 
# class ShowRoom_viewSet(viewsets.ViewSet):
#     def list(self,request):
#         queryset  = ShowRoom.objects.all()
#         serializer = ShowroomSerializer(
#             queryset, many=True, context={"request": request}
#         )
#         return Response(serializer.data)
    
#     def retrieve(self, request,pk):
#         queryset  = ShowRoom.objects.all()
#         data = get_object_or_404(queryset ,pk=pk)
#         serializer = ShowroomSerializer(data,context={"request": request})
#         return Response(serializer.data)
    
#     def create(self,request):
#         serializer = ShowroomSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else:
#             return Response(serializer.errors, status=400)
            
    



# Rest Frame Work 1st Start of Rest Frame Work
@api_view(["GET", "POST"])
def car_list(request):
    if request.method == "GET":
        car_list = CarList.objects.all()
        serializer = CarSerializer(car_list, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serilize = CarSerializer(data=request.data)
        if serilize.is_valid():
            serilize.save()
            return Response(serilize.data, status=201)
        else:
            return Response(serilize.errors, status=400)


@api_view(["GET", "PUT", "DELETE"])
def car_detail(request, pk):
    try:
        # Retrieve the car object, or raise a 404 error if not found
        car = CarList.objects.get(pk=pk)
    except CarList.DoesNotExist:
        return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        # Handle GET request
        serializer = CarSerializer(car)
        return Response(serializer.data)

    elif request.method == "PUT":
        # Handle PUT request
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        # Handle DELETE request
        car.delete()
        return Response(
            {"message": "Car deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )




# Class Based View
# class show_rooms(APIView):

#     # authentication_classes = [BasicAuthentication]
#     # permission_classes = [IsAuthenticated]
#     # authentication_classes = [SessionAuthentication]
#     # permission_classes = [AllowAny]
#     # permission_classes = [IsAdminUser]

#     def get(self, request):
#         showrooms = ShowRoom.objects.all()
#         serializer = ShowroomSerializer(
#             showrooms, many=True, context={"request": request}
#         )
#         return Response(serializer.data)

#     def post(self, request):
#         serilize = ShowroomSerializer(data=request.data)
#         if serilize.is_valid():
#             serilize.save()
#             return Response(serilize.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serilize.errors, status=status.HTTP_400_BAD_REQUEST)


# class showRoom_details(APIView):
#     def get(self, request, pk):
#         try:
#             showroom = ShowRoom.objects.get(pk=pk)
#         except ShowRoom.DoesNotExist:
#             return Response(
#                 {"error": "Showroom not found"}, status=status.HTTP_404_NOT_FOUND
#             )

#         serilizer = ShowroomSerializer(showroom)
#         return Response(serilizer.data)

#     def put(self, request, pk):
#         try:
#             showroom = ShowRoom.objects.get(pk=pk)
#             serializer = ShowroomSerializer(showroom, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except ShowRoom.DoesNotExist:
#             return Response(
#                 {"error": "Showroom not found"}, status=status.HTTP_404_NOT_FOUND
#             )

#     def delete(self, request, pk):
#         try:
#             showroom = ShowRoom.objects.get(pk=pk)
#             showroom.delete()
#             return Response(
#                 {"message": "Showroom deleted successfully"},
#                 status=status.HTTP_204_NO_CONTENT,
#             )
#         except ShowRoom.DoesNotExist:
#             return Response(
#                 {"error": "Showroom not found"}, status=status.HTTP_404_NOT_FOUND
#             )




# Generic and Mixin

# class ReiviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Reivew.objects.all()
#     serializer_class = ReiviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    

# class ReiviewList(
#     mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
# ):
#     queryset = Reivew.objects.all()
#     serializer_class = ReiviewSerializer
#     authentication_classes=[SessionAuthentication]
#     permission_classes=[DjangoModelPermissions]
    
#     def get(self,request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



# Create your views here.
# def car_list(request):
#     car_list = CarList.objects.all()
#     data = {
#         'car_list': list(car_list.values())
#     }
#     # print(car_list)
#     # data = json.dumps(car_list)
#     # return HttpResponse(data, content_type='application/json')
#     return JsonResponse(data)

# def car_detail(request,pk):
#     car_id = CarList.objects.get(pk=pk)
#     data = {
#         'car_name': car_id.car_name,
#         'car_decs':car_id.car_decstr,
#         'car_active' : car_id.active
#     }
#     return JsonResponse(data)
