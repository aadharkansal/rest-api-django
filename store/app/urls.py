from django.urls import path
from . import views

urlpatterns = [
    path('customer/signup/', views.customer_signup,  name='student_signup'),
    path('nursery/signup/', views.nursery_signup,  name='student_signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('plants/',views.PlantListView.as_view()),
    path('plants/<int:pk>',views.PlantDetailView.as_view()),
    path('orders/',views.OrderPlace.as_view()),
    path('orders_view/',views.OrderView.as_view()),
]