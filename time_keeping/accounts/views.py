from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import TimeRecord
from .models import User
from django.urls import reverse

@login_required(login_url='/login/')
def check_in(request):
    if request.method == 'POST':
        if form.is_valid():
            if user is not None:
                if next_url := request.POST.get('next'):
                    return redirect(next_url)
                else:
                    
                    return redirect(reverse('home'))
    
    user = request.user
    current_time = timezone.now()
    TimeRecord.objects.create(user=user, check_in_time=current_time)
    return redirect('home')


@login_required(login_url='/login/')
def check_out(request):
    user = request.user
    current_time = timezone.now()
    time_record = TimeRecord.objects.filter(user=user, check_out_time__isnull=True).first()
    if time_record is not None:
        time_record.check_out_time = current_time
        time_record.save()
    return redirect('home')


# Create your views here.

def home_view(request):

        return render(request, 'check_in.html')

@login_required
def success(request):
    if request.user.is_authenticated:
        return render(request, 'success.html')
    else:
        return render(request, 'check_in.html')
