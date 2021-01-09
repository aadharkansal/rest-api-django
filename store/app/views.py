from rest_framework.response import Response
from . import models,serializers
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView
)

class PlantListView(ListCreateAPIView):
    queryset = models.plant.objects.all()
    serializer_class = serializers.PlantsSerializer

class PlantDetailView(RetrieveUpdateAPIView):
    queryset = models.plant.objects.all()
    serializer_class = serializers.PlantsSerializer

class OrderPlace(CreateAPIView):
    queryset = models.order.objects.all()
    serializer_class = serializers.OrdersSerializer

class OrderView(ListAPIView):
    queryset = models.order.objects.all()
    serializer_class = serializers.OrdersSerializer