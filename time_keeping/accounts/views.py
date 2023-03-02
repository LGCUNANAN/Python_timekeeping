from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.views.generic import ListView
from django.utils import timezone
from django.contrib import messages
from .models import TimeRecord
from .models import User

def time_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None and user.is_authenticated:
            login(request, user)
            time_in = timezone.now()
            print(time_in)
            TimeRecord.objects.create(user=user, time_in=time_in)
            return redirect('accounts:time_out')

        else:
            error_message = "Invalid login credentials"
            return render(request, 'time_in.html', {'error_message': error_message})
    else:
        if request.session.get('time_in'):
            return redirect('accounts:time_out')
        return render(request, 'time_in.html')

def login_redirect(request):
    if request.user.is_authenticated:
        return redirect('accounts:time_out')
    else:
        return redirect('accounts:time_in')
login_required
def time_out(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_authenticated:
            logout(request)
            time_in = user.timerecord_set.latest('time_in').time_in
            time_out = timezone.now()
            TimeRecord.objects.create(user=user, time_in=time_in, time_out=time_out)
            return redirect('accounts:time_in')
        else:
            error_message = "Invalid logout credentials"
            return render(request, 'time_out.html', {'error_message': error_message})
    else:
        return render(request, 'time_out.html')

class TimeRecordListView(ListView):
    model = TimeRecord
    template_name = 'time_record_list.html'