from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from .models import TimeRecord
from .models import User
from django.urls import reverse
from django.http import HttpResponseRedirect

@login_required
def check_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        
        if user is not None and user.is_authenticated:
            
            check_in_time = timezone.now()
            
            TimeRecord.objects.create(user=user, check_in_time=check_in_time)

            login(request, user)

            request.session['email'] = email
            
            success_message = "Successfully Time In"

            redirect_url = reverse('check_out') + f'?success_message={success_message}'
            return redirect(redirect_url)
        else:
            error_message = "Invalid login credentials"
            return render(request, 'check_in.html', {'error_message': error_message})
    else:
        error_message = "Invalid login credential"
        return render(request, 'check_in.html', {'error_message': error_message})
    

@login_required
def check_in_confirm(request):
    email = request.session.get('email')
    return render(request, 'check_in_confirm.html', {'email': email})

@login_required
def check_out(request):
    email = request.session.get('email')
    if email:
        del request.session['email']
    logout(request)
    user = request.user
    check_in_time = timezone.now()
    time_record = TimeRecord.objects.filter(user=request.user, check_out_time__isnull=True).first()
    if time_record is not None:
        time_record.check_out_time = check_in_time
        time_record.save()
    success_message = request.GET.get('success_message')
    return render(request, 'check_out.html', {'success_message': success_message})
