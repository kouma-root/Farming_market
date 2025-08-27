from django.shortcuts import render, redirect
from Product.models import Item
from Request.models import Request
from Users.decorators import buyer_required, farmer_required
from .forms import CustomerUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser

#Register view for all users with status ( Farmers/Buyers)
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
def all_users_view(request):
    users = CustomUser.objects.all().select_related('profile')
    buyers = [user for user in users if hasattr(user, 'profile') and user.profile.is_buyer]
    farmers = [user for user in users if hasattr(user, 'profile') and user.profile.is_farmer]
    return render(request, 'users/allUsers_view.html', {
        'buyers': buyers,
        'farmers': farmers,
    })


#dashboard for farmers
@login_required
@farmer_required
def farmer_dashboard(request):
    user = request.user
    products = Item.objects.filter(owner=user)
    requests_qs = Request.objects.filter(product__in=products)
    stats = {
        'total_products': products.count(),
        'total_requests': requests_qs.count(),
        'pending_requests': requests_qs.filter(status='Pending').count(),
        'approved_requests': requests_qs.filter(status='Approved').count(),
        'rejected_requests': requests_qs.filter(status='Rejected').count(),
        'cancelled_requests': requests_qs.filter(status='Cancelled').count(),
    }
    return render(request, 'users/farmer_dashboard.html', {
        'user': user,
        'products': products,
        'requests': requests_qs,
        'stats': stats,
    })

# Dashboard for buyers
@login_required
@buyer_required
def buyer_dashboard(request):
    user = request.user
    requests_qs = Request.objects.filter(buyer=user)
    stats = {
        'total_requests': requests_qs.count(),
        'pending_requests': requests_qs.filter(status='Pending').count(),
        'approved_requests': requests_qs.filter(status='Approved').count(),
        'rejected_requests': requests_qs.filter(status='Rejected').count(),
        'cancelled_requests': requests_qs.filter(status='Cancelled').count(),
    }
    return render(request, 'users/buyer_dashboard.html', {
        'user': user,
        'requests': requests_qs,
        'stats': stats,
    })