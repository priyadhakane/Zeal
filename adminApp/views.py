from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import ExtendedUser
from studentApp.models import Course
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.models import User

# Create your views here.
def signin(request):
    if request.method == "POST":
        user_type = request.POST['role']
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate( request,username=email, password=password)
        if user is not None:
            ex_user = ExtendedUser.objects.get(user=user.id)
            if ex_user.user_type == user_type:
                print("User Type Correct!")
                # redirect to corresponding dashboard
                if user_type == "admin":
                    login(request, user)
                    return redirect('/')
                elif user_type == "student":
                    login(request, user)
                    return redirect('/student')
                elif user_type == "staff":
                    login(request, user)
                    return redirect('/staff')
        else:
            print("Invalid Credentials!!")
            return redirect('/signin')
        
    return render(request, 'signin.html')



def dashboard(request):
    return render(request, 'adminApp/index.html')


def courses(request):
    courses = Course.objects.all()
    return render(request, 'adminApp/manage_course.html', {'courses': courses})

@login_required
def profile_view(request):
    """View profile details."""
    user_profile = UserProfile.objects.filter(user=request.user)
    return render(request, 'adminApp/profile.html', {'user_profile': user_profile})

@login_required
def profile_update(request):
    """Update user profile without using Django forms."""
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == "POST":
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user_profile.phone = request.POST.get('phone')
        user_profile.address = request.POST.get('address')

        if 'profile_picture' in request.FILES:
            user_profile.profile_picture = request.FILES['profile_picture']

        user.save()
        user_profile.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('profile')

    return render(request, 'adminApp/profile_update.html', {'user_profile': user_profile})

@login_required
def change_password(request):
    """Allow users to change their password."""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep user logged in
            messages.success(request, "Your password has been changed successfully!")
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'adminApp/change_password.html', {'form': form})
