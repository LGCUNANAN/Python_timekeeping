from django.shortcuts import render

def Index(request):
    return render(request, 'time_in.html')


