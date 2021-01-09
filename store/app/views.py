from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import *
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Auth system
User = get_user_model()

def customer_signup(request):
    if request.method == "POST":
        form = customer_signup(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return HttpResponseRedirect('/')
    else:
        form = customer_signup(request.POST)
    return render(request,'/customer/signup',{'form':form})

def nursery_signup(request):
    if request.method == "POST":
        form = nursery_signup(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return HttpResponseRedirect('/')
    else:
        form = nursery_signup(request.POST)
    return render(request,'/nursery/signup',{'form':form})

def user_login(request):
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user:
                        if user.is_customer:
                                login(request, user)
                                return redirect('customer_dashboard')
                        if user.is_nursery:
                                login(request, user)
                                return redirect('nursery_dashboard')
                            
                        else:
                                return render(request, 'inactiv_account.html')
                else:
                        return render(request, 'inactiv_account.html')
        else:
            form = UserLoginForm(request.POST)

        context = {
                'form': form,
        }
        return render(request, 'portal/login.html', context)

def user_logout(request):
    django_logout(request)
    return redirect('/')


# rest framework rest-api

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