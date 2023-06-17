from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect



# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:

            if User.objects.filter(username=username).exists():
                messages.info(request, "username Taken")
                return redirect('credentials:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Taken")
                return redirect('credentials:register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save()
                messages.info(request, "User Registered")
                return redirect('credentials:login')
        else:
            messages.info(request,"password not matching")
            return redirect('credentials:register')
        return redirect('cart:login')
    return render(request,"register.html")


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, "Invalid Credentials")
            return redirect('credentials:login')

    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')