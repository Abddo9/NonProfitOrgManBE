
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import numpy as np
import cv2
import os
from .models import ProductRecord, Product, Event, Volunteer

from .visionapi import detect_and_count_objects

@csrf_exempt
def detect_and_count(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        image_path = default_storage.save('temp.jpg', image_file)
        image = cv2.imread(image_path)
        classes = request.POST.get('classes', None)
        result = detect_and_count_objects(image, classes)
        return JsonResponse(result)
    return JsonResponse({'error': 'Invalid request'}, status=400)


def get_products(request):
    product_records = Product.objects.all()
    return JsonResponse([{"id": record.id,
                            "name": record.name,
                            "description": record.description,
    } for record in product_records], safe=False)


def get_products_records(request):
    product_records = ProductRecord.objects.all()
    return JsonResponse([{
        'id': record.id,
        'product_id': record.product.id,
        'product': record.product.name,
        'source': record.source,
        'quantity': record.quantity,
        'recived_on': record.recived_on,
        'expires_on': record.expires_on,
    } for record in product_records], safe=False)

def get_volunteers(request):
    volunteers = Volunteer.objects.all()
    return JsonResponse([{
        'id': volunteer.id,
        'full_name': volunteer.full_name,
        'email': volunteer.email,
        'phone': volunteer.phone,
        'availabilities': ",".join([str(av.id) for av in volunteer.availabilities.all()]),
        'events': ",".join([str(e.id) for e in volunteer.events.all()]),
    } for volunteer in volunteers], safe=False)

def index(request):
    return HttpResponse("Hello, world. You're at the non profit management index.")

