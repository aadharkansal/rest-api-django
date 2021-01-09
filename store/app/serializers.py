from rest_framework import serializers
from . import models

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customer
        fields = "__all__"

class NurserySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.nursery
        fields = "__all__"

class PlantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.plant
        fields = "__all__"

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.order
        fields = "__all__"