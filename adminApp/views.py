from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def signin(request):
    if request.method == "POST":
        user_type = request.POST['role']
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate( request,username=email, password=password)
        if user is not None:
            if user.ExtendedUser.user_type == user_type:
                print("User Type Correct!")
            login(request, user)
            print("User logged In", user)
            return redirect('/')
        else:
            print("Invalid Credentials!!")
            return redirect('/auth')
        
    return render(request, 'signin.html')



def dashboard(request):
    return render(request, 'base.html')