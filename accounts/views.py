from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from accounts.models import User
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import EmailMessage
from profiles.models import *

def RegisterAccount(request):
    users = User.objects.all()
    return render(request, "account/register_account.html", {'users':users})
    
def LoginAccount(request):
    err_mess = ""
    if request.method =="POST":
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request,user)
            messages.success(request, f'Log In Successfully')
            create_account(request)
            return redirect('home')
        else:
            err_mess = "Invalid Username and Password or User does not exist"
    context = {'err_mess' : err_mess}
    return render(request, "account/login.html", context)

def ConfirmAccount(request):
    if request.method == "POST":
        otp = generateOTP()
        context={'email':request.POST['email'],
                 'username':request.POST['username'],
                 'pass':request.POST['pass1'],
                 'otp': otp}
        send_OTP(request.POST['username'], request.POST['email'], otp)
    return render(request, "account/verify_account.html", context)

def CreateAccount(request):
    User.objects.create_user(
        username=request.POST['username'], 
        password=request.POST['password'], 
        email=request.POST['email']) 
    messages.success(request, f'Account created successfully. Please Log In using that account')
    return redirect('login')


def LogoutAccount(request):
    logout(request)
    messages.success(request, f'Log Out Successfully')
    return redirect('login')


def generateOTP():
    return f'{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'

def send_OTP(username, user_email, otp):
    message = f'Good day {username}!,\n\nThis is the OTP for your MalayanFolio Account {otp}.\n\nIf this was not requested by you, you can ignore this email.'
    email = EmailMessage(
        'MalayanFolio Account OTP',#subject
        message,#message
        to=[user_email],) #to
    email.fail_silenty=False
    email.send()

def create_account(request):
    #User Account
    try:
        user_profile = UserProfile.objects.get(user_id = request.user.id)
    except Exception as e:
        #create default account
        UserProfile.objects.create(
            user_id = request.user,
            email = request.user.email
        )

    #User outputs
    try:
        user_outputs = Outputs.objects.get(user_id = get_User_id(request))
    except Exception as e:
        #create default
        Outputs.objects.create(
            user_id = get_User_id(request),
        )

    #user Education
    user_educ = Education.objects.filter(user_id = get_User_id(request))
    if user_educ.count() < 4:
        Education.objects.create(
            user_id = get_User_id(request),
            educ_type = "PS"
        )
        Education.objects.create(
            user_id = get_User_id(request),
            educ_type = "GS"
        )
        Education.objects.create(
            user_id = get_User_id(request),
            educ_type = "HS"
        )
        Education.objects.create(
            user_id = get_User_id(request),
            educ_type = "SHS"
        )
       

    #User Languages 
    

    #User Extracurricular

    #User Interests
    


def get_User_id(request):
    user_profile = UserProfile.objects.get(user_id = request.user.id)
    return user_profile


