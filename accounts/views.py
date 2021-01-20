from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import SignUpForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have Been Logged In!'))
            return redirect('home')
        else:
            messages.error(request, ('Error Logging In - Please try again!'))
            return redirect('login')
    else:
        return render(request, 'includes/login.html')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('You have Registered'))
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'includes/register.html', context)


def logout_user(request):
    logout(request)
    messages.error(request, ('You have Been Logged Out..'))
    return redirect('home')

def edit_profile(request):
    pass
