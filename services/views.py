from django.shortcuts import render,redirect
from django.http import HttpResponse
from services.forms import FixtureForm
from .models import Fixture
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordResetForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from  django.contrib.auth.models import User


def home(request):
    fixtures=Fixture.objects.all()
    usernew=User.objects.all()
    number=len(usernew)
    return render(request,'home.html',{'fixtures':fixtures,'userno':number})


def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    
    form=UserCreationForm()
    return render(request,'register.html',{'form':form})


def loginpage(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.cleaned_data.get('username')
            passw=form.cleaned_data.get('password')
            userlog=authenticate(username=user,password=passw)
            if userlog is not None:
                login(request,userlog)
                return redirect('home') 

    form=AuthenticationForm(request,data=request.POST)
    return render(request,'login.html',{'form':form})
def logoutpage(request):
    logout(request)
    return redirect('login')

def update(request,id):
    if request.method=="POST":
        id=Fixture.objects.get(pk=id)
        form=FixtureForm(request.POST,instance=id)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    id=Fixture.objects.get(pk=id)
    form=FixtureForm(instance=id)
    return render(request,'update.html',{'form':form})

def delete(request,id):
    id=Fixture.objects.get(pk=id)
    id.delete()
    fixture=Fixture.objects.all()
    return render(request,'home.html',{'fixture':fixture})


def create(request):
    if request.method=="POST":
        form=FixtureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    form=FixtureForm(request.POST)
    return render(request,'update.html',{'form':form})

    