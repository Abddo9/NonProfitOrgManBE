from django.urls import path,re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("detect_and_count", views.detect_and_count, name="detect_and_count"), 
    re_path('^products(?:/(?P<id>\d+))?/$', views.products, name="products"), 
    path("volunteers", views.volunteers, name="volunteers"), 
    path("products_records", views.products_records, name="products_records"), 
    path("events", views.events, name="events"), 
]