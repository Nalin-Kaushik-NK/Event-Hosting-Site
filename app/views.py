from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Registration
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import authenticate


def index(request):
    return render(request, 'index.html')


def signup(request):
    return render(request, 'signup.html')


@csrf_exempt
def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        degree = request.POST.get('degree')
        branch = request.POST.get('branch')
        enroll = request.POST.get('enrollment')

        if Registration.objects.filter(email=email):
            messages.error(request, "Alert! This email is already registered")
            return redirect('signup')

        if Registration.objects.filter(enroll=enroll):
            messages.error(request, "Alert! Enrollement is already registered")
            return redirect('signup')

        if pass1 != pass2:
            messages.error(
                request, "Alert! Please make sure your password is same in Confirm Password")
            return redirect('signup')

        if len(pass1) <= 8 or not (any(chr.isdigit() for chr in pass1)):
            messages.error(
                request, "Alert! Password length should by greater than 8 and must contain a digit!!")
            return redirect('signup')

        myuser = Registration(enroll=enroll, password=pass1, email=email, first_name=fname,
                              last_name=lname, gender=gender, degree=degree, branch=branch)

        myuser.save()
        messages.success(
            request, "Congratulations.🙌 Your Account has been successfully created.")
        return redirect('index')

    return redirect('signup')


@csrf_exempt
def login(request):
    if request.method == "POST":
        enroll = request.POST.get('enroll')
        password = request.POST.get('password')

        print('ch1')
        user = authenticate(username=enroll, password=password)
        if user is not None:
            print('ch2.0')
            login(request, user)
            print('ch2')
            return render(request, 'home.html')
        else:
            redirect('index')
        print('ch3')
    redirect('index')


def home(request):
    return render(request, 'home.html')

# Create your views here.
