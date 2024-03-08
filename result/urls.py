from result.views import *
from django.urls import path

urlpatterns = [
    path('',index,name='index'),
    path('teachers_login',teachers_login, name='teachers'),
    path('selection_page' , selection , name='selection_page'),
    path('dataview_page', dataview , name='dataview_page'),
    path('logout' , logoutuser, name='logout_page'),
    path('Verify-user', verify ,name='forgot_password'),
    path('generate_password', forgot, name="generate_password"),
    path('inputdata' ,datainput, name='data_input'),
    path('signupteachers', signup_teachers, name='signup_teachers'),
    path('singupstudents', signup_students, name='signup_students')
]