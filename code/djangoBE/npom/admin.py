from django.contrib import admin

from .models import ProductRecord,Event,Product,Volunteer

admin.site.register(Product)
admin.site.register(ProductRecord)
admin.site.register(Volunteer)
admin.site.register(Event)
