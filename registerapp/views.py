from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import user


# Create your views here.

def RegisterPage(request):
    return render(request, 'register.html')


def User_Register(request):
    if request.method == 'POST':
        Firstname = request.POST.get('fname')
        Lastname = request.POST.get('lname')
        Email = request.POST.get('email')
        Contact = int(request.POST.get('contact'))
        Password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if Password != cpassword:
            return HttpResponse('password and confirm password are not same..')
        else:
            emaildata = user.objects.values_list('Email')
            if Email in emaildata:
                return HttpResponse("USER Already Exists ...")
            else:
                en = user(Firstname=Firstname, Lastname=Lastname, Email=Email, Contact=Contact, Password=Password)
                en.save()
                return render(request, 'login.html')


def final(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        e_data = user.objects.values_list('Email').values()
        if email == e_data:
            password_data = user.objects.filter('email').values()
            if password_data == password:
                return HttpResponse('you are a valid uer')
            else:
                message = 'email id or password does not match....'
                return render(request, 'login.html', {'msg': message})
        else:
            return HttpResponse('Not a registered user')
