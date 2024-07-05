from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def loanapply(request):
   
    
    return render(request,"loanapply.html")
def loan_apply1(request):
    return render(request,'loanapply.html')
def index(request):
    return render(request,"index.html")

def logout_user(request):
    logout(request)
    return redirect('index')
def login_user(request):
    if request.method == 'POST':
       
        username = request.POST.get('username')
        password = request.POST.get('password')
        
       
        user = authenticate(username=username, password=password)
        
        if user is not None:
           
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('index')  
        else:
            
            messages.error(request, 'Invalid username or password.')
            return redirect('login_user') 
    
    return render(request, 'login_user.html')  
    
    
def register(request):
    if request.method == 'POST':
       
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
            
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return redirect('register')
        
       
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'User registered successfully!')
            return redirect('index')  
        except IntegrityError as e:
            messages.error(request, f'Error occurred: {str(e)}')
            
            return redirect('register') 
    
    return render(request, 'login_user.html')  