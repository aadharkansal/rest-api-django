from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe

# Create your models here.

class User(AbstractUser):
	is_customer=models.BooleanField(default=False)
	is_nursery=models.BooleanField(default=False)

class customer(models.Model):
    created = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20,null=False,blank=False)
    email = models.EmailField(max_length=50,null=False,blank=False)
    address = models.CharField(max_length=50,blank=False)
    mob = models.IntegerField(blank=False)
    def __str__(self):
		    return self.name

class nursery(models.Model):
    name = models.CharField(max_length=20,null=False,blank=False)
    email = models.EmailField(max_length=50,null=False,blank=False)
    address = models.CharField(max_length=50,blank=False)
    mob = models.IntegerField(blank=False)
    def __str__(self):
		    return self.name

class plant(models.Model):
    name = models.CharField(max_length=15,null=False,blank=False)
    price = models.CharField(max_length=4)
    img = models.ImageField(upload_to='plantimages',null=True,blank=True)
    def __str__(self):
		    return self.name

class order(models.Model):
    name = models.CharField(max_length=20,blank=False)
    address = models.CharField(max_length=50,blank=False,null=True)
    mob = models.IntegerField(blank=False,null=True)
    plant_ordered = models.CharField(max_length=15,null=True)
    def __str__(self):
		    return self.name