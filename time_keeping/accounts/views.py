from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.utils import timezone
from django.contrib import messages
from .models import TimeRecord
from .models import User

def check_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None and user.is_authenticated:
            login(request, user)
            check_in_time = timezone.now()
            time_record = user.timerecord_set.latest('check_in_time')

            TimeRecord.objects.create(user=user, check_in_time=check_in_time)

            return redirect('accounts:check_out')

        else:
            error_message = "Invalid login credentials"
            return render(request, 'check_in.html', {'error_message': error_message})
    else:
        if request.session.get('check_in'):
            return redirect('accounts:check_out')
        return render(request, 'check_in.html')

def login_redirect(request):
    if request.user.is_authenticated:
        return redirect('accounts:check_out')
    else:
        return redirect('accounts:check_in')

def check_out(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        print(email)
        print(password)
        user = authenticate(email=email, password=password)
        if user is not None and user.is_authenticated:
            logout(request)
            check_in_time = user.timerecord_set.latest('check_in_time').check_in_time
            check_out_time = timezone.now()
            TimeRecord.objects.create(user=user, check_in_time=check_in_time, check_out_time=check_out_time)
            return redirect('accounts:check_in')
        else:
            error_message = "Invalid logout credentials"
            return render(request, 'check_out.html', {'error_message': error_message})
    else:
        return render(request, 'check_out.html')

