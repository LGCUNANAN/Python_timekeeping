from django.shortcuts import render

def Index(request):
    return render(request, 'check_in.html')


