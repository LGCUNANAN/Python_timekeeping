from django.shortcuts import render,redirect

def Index(request):
    if request.session.get('loggedin'):
        return redirect('accounts:time_out')
    return render(request, 'time_in.html')


