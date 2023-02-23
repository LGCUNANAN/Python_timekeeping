from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from accounts.models import Employee
from django.contrib.auth import authenticate, login,logout  
from django.contrib import messages
from django.contrib.auth.models import User

def Index(request):
    context_dict = {}

    employees = Employee.objects.all()

    context_dict["employees"] = employees

    return render(request, 'login.html', context=context_dict)
def Logout(request):
    context_dict = {}

    employees = Employee.objects.all()

    context_dict["employees"] = employees

    return render(request, 'base.html', context=context_dict)

def Login(request):
    context_dict = {}

    employees = Employee.objects.all()

    context_dict["employees"] = employees

    return render(request, 'logout.html', context=context_dict)
