from django.shortcuts import render
from .models import CarList
from django.http import JsonResponse,HttpResponse
import json

# Create your views here.
def car_list(request):
    car_list = CarList.objects.all()
    data = {
        'car_list': list(car_list.values())
    }
    # print(car_list)
    # data = json.dumps(car_list)
    # return HttpResponse(data, content_type='application/json')
    return JsonResponse(data)

def car_detail(request,pk):
    car_id = CarList.objects.get(pk=pk)
    data = {
        'car_name': car_id.car_name,
        'car_decs':car_id.car_decstr,
        'car_active' : car_id.active
    }
    return JsonResponse(data)