from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import  auth, User


# Create your views here.
def home(request):
    return render(request,'home.html')


def submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['emailid']
        phonenumber = request.POST['number']

        user = User.objects.create_user(name, email, phonenumber)
        user.save();
        print("user created")
        return redirect('/')


    return render(request,'result.html')

















