from result.views import *
from django.urls import path , re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',index,name='index'),
    path('teachers_login',teachers_login, name='teachers'),
    path('selection_page' , selection , name='selection_page'),
    path('dataview_page', dataview , name='dataview_page'),
    path('logout' , logoutuser, name='logout_page'),
    path('verify_user', verify_email ,name='verify'),
    path('reset-password/<uid>/<token>/', reset_password, name='reset_password'),
    path('inputdata' ,datainput, name='data_input'),
    path('signupteachers', signup_teachers, name='signup_teachers'),
    path('signupstudents', signup_students, name='signup_students'),
    path('student_login' , student_login, name='student_login'),
    path('service_page' , service, name='service'),
    path('update-notice' , update_notice, name='update_notice'),
    path('forgot' , forgot , name='forgot'),
    re_path(r'^.*/$', custom_404_page),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)