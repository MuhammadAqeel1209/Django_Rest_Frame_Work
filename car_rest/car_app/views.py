from django.shortcuts import render
from .models import CarList
# from django.http import JsonResponse,HttpResponse
# import json
from .api_file.serialization import CarSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

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


# Rest Frame Work

@api_view(['GET','POST'])
def car_list(request):
    if request.method == 'GET':
        car_list = CarList.objects.all()
        serializer = CarSerializer(car_list, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serilize = CarSerializer(data = request.data)
        if serilize.is_valid():
            serilize.save()
            return Response(serilize.data, status=201)
        else:
            return Response(serilize.errors, status=400)

@api_view(['GET','PUT','DELETE'])
def car_detail(request, pk):
    try:
        # Retrieve the car object, or raise a 404 error if not found
        car = CarList.objects.get(pk=pk)
    except CarList.DoesNotExist:
        return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Handle GET request
        serializer = CarSerializer(car)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Handle PUT request
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Handle DELETE request
        car.delete()
        return Response({"message": "Car deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
