from django.contrib import admin
from . import models
# Register your models here.
admin.site.register([
    models.customer,
    models.nursery,
    models.plant,
    models.order
])