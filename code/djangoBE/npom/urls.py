from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("detect_and_count", views.detect_and_count, name="detect_and_count"), 
    path("get_products", views.get_products, name="get_products"), 
    path("get_volunteers", views.get_volunteers, name="get_volunteers"), 
    path("get_products_records", views.get_products_records, name="get_products_records"), 
    path("get_products_records", views.get_products_records, name="get_products_records"), 
]