from django.urls import path
from . import views

urlpatterns = [
    path('plants/',views.PlantListView.as_view()),
    path('plants/<int:pk>',views.PlantDetailView.as_view()),
    path('orders/',views.OrderPlace.as_view()),
    path('orders_view/',views.OrderView.as_view()),
]