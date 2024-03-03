from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from result.models import *
from result.forms import *


# Create your views here.

def index(request):
        if request.method=="POST":
             username = request.POST.get('username')
             password = request.POST.get('password')
             user= authenticate(username = username, password= password)
             if user is not None:
               login(request, user)
               messages.success(request, "!!!! you are loged in successfully !!!!!")
               return redirect("selection_page")

             else:
                messages.success(request, "!!!! username or password is invalid !!!!!")
                return render(request, 'index.html')  
        else:
            return render(request, 'index.html')
        

def teachers_login(request):
        if request.method=="POST":
             username = request.POST.get('username')
             password = request.POST.get('password')
             user= authenticate(username = username, password= password)
             if user is not None:
                login(request, user)
                messages.success(request, "!!!! you are loged in successfully !!!!!")
                return redirect("selection_page")

             else:
                messages.success(request, "!!!! username or password is invalid !!!!!")
                return redirect("teachers_login")   
        else:
            return render(request, 'teachers_login.html')
@login_required
def selection(request):
     if request.method=="POST":
          return redirect("dataview_page")
     else:
          return render(request, 'selection_page.html')
@login_required    
def dataview(request):
          data=examResult.objects.all()
          return render(request, 'dataview.html', {'data' :data})

def logoutuser(request):
      logout(request)
      return redirect("/")

def verify(request):
     if request.method=="POST":
          return redirect("generate_password")
     return render(request, 'verify_user.html')

def forgot(request):
     return render(request, 'forgot.html')