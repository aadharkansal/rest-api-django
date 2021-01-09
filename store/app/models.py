from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe

# Create your models here.

class customer(models.Model):
    name = models.CharField(max_length=20,blank=False)
    address = models.CharField(max_length=50,blank=False)
    mob = models.IntegerField(max_length=10,blank=False)

class nursery(models.Model):
    name = models.CharField(max_length=20,blank=False)
    address = models.CharField(max_length=50,blank=False)
    mob = models.IntegerField(max_length=10,blank=False)

class plant(models.Model):
    name = models.CharField(max_length=15)
    price = models.CharField(max_length=4)
    img = models.ImageField(upload_to='plantimages',null=True,blank=True)

class order(models.Model):
    # order_name = models.ForeignKey(customer,on_delete=models.CASCADE)
    name = models.CharField(max_length=20,blank=False)
    address = models.CharField(max_length=50,blank=False,null=True)
    mob = models.IntegerField(max_length=10,blank=False,null=True)
    plant_ordered = models.CharField(max_length=15,null=True)