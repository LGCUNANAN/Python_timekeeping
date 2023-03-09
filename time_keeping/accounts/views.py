from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.utils import timezone
from .models import TimeRecord
from django.contrib import messages

def time_in(request):
    if request.session.get('loggedin'):
        return redirect('accounts:time_out')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_authenticated:
                login(request, user)
                time_in = timezone.now()
                request.session['loggedin'] = True
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

@login_required
def time_out(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_authenticated:
            if user == request.user:
                logout(request)
                previous_record = user.timerecord_set.latest('time_in')
                time_in = previous_record.time_in
                previous_record.delete()
                time_out = timezone.now()
                duration = time_out - time_in
                hours, remainder = divmod(duration.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                TimeRecord.objects.create(user=user, time_in=time_in, time_out=time_out)
                message = f'Your Time Out is Successfully Recorded. \nYour time in was {time_in.strftime("%I:%M:%S %p")} and your time out was {time_out.strftime("%I:%M:%S %p")}. Your total time for this day was {hours} hours and {minutes:02d} minutes.'
                messages.success(request, message)
                return redirect('accounts:time_in')
            else:
                error_message = "Invalid logout credentials"
                return render(request, 'time_out.html', {'error_message': error_message})
        else:
            error_message = "Invalid login credentials"
            return render(request, 'time_out.html', {'error_message': error_message})
    else:
        time_records = request.user.timerecord_set.all().order_by('-time_in')
        context = {'time_records': time_records}
        return render(request, 'time_out.html', context)


class TimeRecordListView(ListView):
    model = TimeRecord
    template_name = 'time_record_list.html'
