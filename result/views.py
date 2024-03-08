from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User,Group
from result.models import *
from result.forms import *


# Create your views here.

def index(request):
        if request.method=="POST":
             #takes the input by user and it following variables
             username = request.POST.get('username')
             password = request.POST.get('password')
             #here is authenticate the username anad password
             user= authenticate(username = username, password= password)
             # it checks wheather the enter creadentials are from student group or not 
             if user is not None and user.groups.filter(name='Students').exists():
               login(request, user)
               return redirect("selection_page")

             else:
                messages.success(request, "!!!! username or password is invalid !!!!!")
                print(messages.get_messages(request))
                return render(request, 'index.html')  
        else:
            return render(request, 'index.html')
        

def teachers_login(request):
         if request.method=="POST":
             username = request.POST.get('username')
             password = request.POST.get('password')
             user= authenticate(username = username, password= password)
             if user is not None and user.groups.filter(name='Teachers').exists():
                login(request, user)
                return redirect("/inputdata")

             else:
                messages.success(request, "!!!! username or password is invalid !!!!!")
                return render(request, 'teachers_login.html')   
         else:
            return render(request, 'teachers_login.html')
         
@login_required
def datainput(request):
          if request.method=="POST":
               Name=request.POST.get('Name')
               Enrollment=request.POST.get('Enrollment')
               C_id=request.POST.get('c_id')
               C_name=request.POST.get('c_name')
               branch=request.POST.get('branch')
               Sem=request.POST.get('sem')
               exam_type=request.POST.get('exam_type')
               Sub1=request.POST.get('sub1')
               M1=request.POST.get('m1')
               # pdf_files1=request.FILES.get('pdf_file1')
               Sub2=request.POST.get('sub2')
               M2=request.POST.get('m2')
               # pdf_files2=request.FILES.get('pdf_file2')
               Sub3=request.POST.get('sub3')
               M3=request.POST.get('m3')
               # pdf_files3=request.FILES.get('pdf_file3')
               Sub4=request.POST.get('sub4')
               M4=request.POST.get('m4')
               # pdf_files4=request.FILES.get('pdf_file4')
               Sub5=request.POST.get('sub5')
               M5=request.POST.get('m5')
               # pdf_files5=request.FILES.get('pdf_file5')
               totaling=request.POST.get('total')
               result=request.POST.get('result')
               email=request.user.email
               content=Result(student_name=Name , enrollment_no=Enrollment ,
                               course_id= C_id , course_name=C_name , Branch=branch , 
                               semester=Sem , exam=exam_type , subject1=Sub1 , marks1=M1 ,
                               #pdf1=pdf_files1 ,
                               subject2=Sub2 , marks2=M2 ,
                              #    pdf2=pdf_files2 ,
                               subject3=Sub3 , marks3=M3 ,
                              #    pdf3=pdf_files3 ,
                                 subject4=Sub4 , marks4=M4 , 
                              #    pdf4=pdf_files4 ,
                                 subject5=Sub5 , marks5=M5 , 
                              #  pdf5=pdf_files5 ,
                               Total=totaling , res=result , email=email )
               content.save()
               messages.success(request, "!!!! Data uploaded successfully !!!!!")
               return render(request, 'input_data.html')
          else:
               return render(request, 'input_data.html')

@login_required
def selection(request):
     if request.method=="POST":
          Course=request.POST.get('course')
          examType=request.POST.get('exam_type')
          sem=request.POST.get('semester')
          enrollment= request.user.username

          if Result.objects.filter(course_id=Course , exam=examType, semester=sem , enrollment_no=enrollment).exists():
              results=Result.objects.filter(course_id=Course , exam=examType, semester=sem , enrollment_no=enrollment)
              context={'results':results}

              return render(request, 'dataview.html', context)
          else:
                messages.success(request, "!!!! course or semster or exam_type does not exist !!!!!")
                return render(request, 'selection_page.html')
     else:
          return render(request, 'selection_page.html')
     

@login_required    
def dataview(request):
          return render(request, 'dataview.html')



def logoutuser(request):
      logout(request)
      return redirect("/")



def verify(request):
     if request.method=="POST":
          return redirect("generate_password")
     return render(request, 'verify_user.html')


def forgot(request):
     return render(request, 'forgot.html')

def signup_teachers(request):
     try:
         if request.method=='POST':
             # take input from the form and store it following variables
             username=request.POST.get('username')
             first=request.POST.get('first')
             last=request.POST.get('last')
             mail=request.POST.get('email')
             password=request.POST.get('password')
             confirm_password=request.POST.get('confirm_password')
             group_name=request.POST.get('user_type')
             #checks if the email provided is already exist in the database
             if User.objects.filter(email=mail).exists():
               return render(request, 'signup_teachers.html', {'error_message': 'Email is already in use'})
             
             if User.objects.filter(username=username).exists():
               return render(request, 'signup_teachers.html', {'error_message': 'username is already in use'})
             # checks if password and confirm password is diffrent or same
             if password != confirm_password:
                return render(request, 'signup_teachers.html', {'error_message': 'Passwords do not match'})
               # create and save a new user in the database
             user = User.objects.create_user(username=username, email=mail, password=password , first_name=first , last_name=last)
             
             # Add the user to the specified group
             group = Group.objects.get(name=group_name)
             user.groups.add(group)
             return redirect("/teachers_login")
     except:
          return HttpResponse("Something went wrong try again")

     return render(request, 'signup_teachers.html')


def signup_students(request):
     try:
          if request.method=='POST':
             username=request.POST.get('username')
             first=request.POST.get('first')
             last=request.POST.get('last')
             mail=request.POST.get('email')
             password=request.POST.get('password')
             confirm_password=request.POST.get('confirm_password')
             group_name=request.POST.get('user_type')
        
             if User.objects.filter(email=mail).exists():
                 return render(request, 'signup_students.html', {'error_message': 'Email is already in use'})
            
             if User.objects.filter(username=username).exists():
                 return render(request, 'signup_teachers.html', {'error_message': 'username is already in use'})
            
             if password != confirm_password:
               return render(request, 'signup_students.html', {'error_message': 'Passwords do not match'})
              
             user = User.objects.create_user(username=username, email=mail, password=password , first_name=first , last_name=last)
             group = Group.objects.get(name=group_name)
             user.groups.add(group)
             return redirect("/")
     except:
          return HttpResponse("Something went wrong try again")

     return render(request, 'signup_students.html')
