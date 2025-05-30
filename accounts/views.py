from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegisterForm

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Ro‘yxatdan muvaffaqiyatli o‘tdingiz!')
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Login yoki parol noto‘g‘ri!')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')