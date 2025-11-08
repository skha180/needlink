# core/viewss/web_views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import CustomUser


def home(request):
    return render(request, 'core/home.html')


# ============================
# Registration
# ============================
def register_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('register_page')

        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            user_type=user_type
        )
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login_page')

    return render(request, 'core/register.html')


# ============================
# Login
# ============================
def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.email}!")
            return redirect("profile_page")
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, "core/login.html")


# ============================
# Logout
# ============================
def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login_page')


# ============================
# Profile (requires login)
# ============================
@login_required(login_url='/login/')
def profile_page(request):
    return render(request, 'core/profile.html', {'user': request.user})

    # edit profile
    
@login_required(login_url='login_page')
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')

        if full_name:
            user.full_name = full_name
        if phone:
            user.phone = phone

        if 'profile_image' in request.FILES:
            user.profile_image = request.FILES['profile_image']

        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile_page')

    return render(request, 'core/edit_profile.html', {'user': user})
