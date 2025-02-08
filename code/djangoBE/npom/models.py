from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=2500)

    def __str__(self):
        return self.name

class ProductRecord(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    source = models.CharField(max_length=500)
    quantity = models.IntegerField(default=1)
    recived_on = models.DateTimeField("recived on")
    expires_on = models.DateTimeField("expires on")
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return str(self.quantity) + "- " +  self.product.name + " - " + self.source

class Availability(models.Model):
    starts_on = models.DateTimeField("start on")
    ends_on = models.DateTimeField("end on")
    def __str__(self):
        return self.starts_on.strftime("%Y-%m-%d %H:%M:%S") + " to " + self.ends_on.strftime("%Y-%m-%d %H:%M:%S")

class Volunteer(models.Model):
    full_name = models.CharField("full name", max_length=500)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    availabilities = models.ManyToManyField(Availability, related_name='volunteers')

    def __str__(self):
        return self.full_name


class Event(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=2500)
    date = models.DateTimeField("event date")
    location = models.CharField(max_length=500)
    volunteers = models.ManyToManyField(Volunteer, related_name='events')

    def __str__(self):
        return self.name + " - " + self.location

