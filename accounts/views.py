from django.shortcuts import render

def register(request):
    return render(request, 'includes/register.html')

def login(request):
    return render(request, 'includes/login.html')