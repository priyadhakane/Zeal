from django.shortcuts import render

# Create your views here.
def signin(request):
    return render(request, 'signin.html')



def dashboard(request):
    return render(request, 'base.html')