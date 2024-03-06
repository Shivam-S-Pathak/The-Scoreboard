from django.contrib import messages
from django.http import HttpResponse
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
               contact=request.POST.get('mobile')
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
                               Total=totaling , res=result, mobile=contact)
               content.save()
               return redirect("/successfull")
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
               return HttpResponse("course or semster or exam does not exist")
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

def success(request):
     return render(request, 'successfull.html')