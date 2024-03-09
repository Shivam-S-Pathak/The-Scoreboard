from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User,Group


from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode
from django.utils.encoding import force_bytes

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
               return redirect("/selection_page")

             else:
                messages.error(request, "!!!! username or password is invalid !!!!!")
                print(messages.get_messages(request))
                return redirect("/") 
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
                messages.error(request, "!!!! username or password is invalid !!!!!")
                return redirect("/teachers_login")   
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
               return redirect("/inputdata")
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
                return redirect("/selection_page")
     else:
          return render(request, 'selection_page.html')
     

@login_required    
def dataview(request):
          return render(request, 'dataview.html')



def logoutuser(request):
      logout(request)
      return redirect("/")



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
               messages.error(request, 'Email is already in use')
               return redirect("/signupteachers")
             
             if User.objects.filter(username=username).exists():
                    messages.error(request, 'username is already in use')
                    return redirect("/signupteachers")
             # checks if password and confirm password is diffrent or same
             if password != confirm_password:
                messages.error(request, 'Passwords do not match')
                return redirect("/signupteachers")
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
                 messages.error(request, 'Email is already in use')
                 return redirect("/signupstudents")
            
             if User.objects.filter(username=username).exists():
                 messages.error(request, 'username is already in use')
                 return redirect("/signupstudents")
            
             if password != confirm_password:
               messages.error(request, 'Passwords do not match')
               return redirect("/signupstudents")
              
             user = User.objects.create_user(username=username, email=mail, password=password , first_name=first , last_name=last)
             group = Group.objects.get(name=group_name)
             user.groups.add(group)
             return redirect("/")
     except:
          return HttpResponse("Something went wrong try again")

     return render(request, 'signup_students.html')




def verify_email(request):
          if request.method=='POST':
               email=request.POST.get('email')
               user=User.objects.filter(email=email).first()
               
               if user:
                     token = default_token_generator.make_token(user)
                     uid = urlsafe_base64_encode(force_bytes(user.pk))
                     reset_link = f"http://127.0.0.1:8000/reset-password/{uid}/{token}/"
                     print(reset_link)
                     msg = EmailMultiAlternatives(
                           subject='Password Reset',
                         #   body=render_to_string('reset_email.html', {'reset_link': reset_link}),
                           from_email='noreply.result.mail@gmail.com',
                           to=[email],
                     )
                     msg.attach_alternative(render_to_string('reset_email.html', {'reset_link': reset_link}), 'text/html')
                     msg.send()
                     messages.success(request, "Email sent successfully")
                     return redirect("/verify_user")
          
               else:
                    messages.error(request, "!!!! Email does not exist !!!!!")
                    return redirect("/verify_user")
               
          else:
               return render(request, 'verify_user.html')
          
          

def reset_password(request, uid, token):
     try:
        # Decode the uid to get the user's primary key (pk)
        uid = urlsafe_base64_decode(str(uid))
        user = User.objects.get(pk=uid)
     except (ValueError, OverflowError, User.DoesNotExist):
         user = None

    # Validate the user and token
     if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            # get password submitted with new password
           password=request.POST.get('password')
           confirm_password=request.POST.get('confirm_password')
           if password !=confirm_password :
                messages.error(request, 'Passwords does not match')
                return redirect("/forgot_password")
           else:
                user.set_password(password)
                user.save()
                login(request, user)
                messages.success(request, 'Your password has been successfully reset.')
                return redirect('/')
        else:
            # Display password reset form
          return render(request, 'forgot.html')
     else:
        # Invalid user or token, display error message and redirect
        messages.error(request, 'The link is invalid or has expired.')
        return redirect('/verify_user')
     

def forgot(request):
     return render(request, "forgot.html")     