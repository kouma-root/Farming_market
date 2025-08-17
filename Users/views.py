from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import CustomerUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser

#Register view for all user with status ( Farmers/Buyers)
def register_view(request):
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # for hashing
            user.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomerUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

#Login view for all users
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')   
        password = request.POST.get('password')

        # Use email because its required as Username
        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect('index')
        else:   
            messages.error(request, "Invalid credentials. Please check your email and password.")
            return redirect('login') 
        
    return render(request, 'users/login.html')

#Logout View
def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def allUsers_view(request):
    users = CustomUser.objects.all()
    return render(request, 'users/allUsers_view.html', context={'users': users})
