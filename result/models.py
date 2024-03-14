from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


# Create your models here.

class Result(models.Model):
    student_name=models.CharField(max_length=40, default='0')
    enrollment_no=models.CharField(max_length=40, default='0')
    course_id=models.CharField(max_length=30, default='0')
    course_name=models.CharField(max_length=30, default='0')
    Branch=models.CharField(max_length=30, default='0')
    semester=models.IntegerField( default='0')
    exam=models.CharField(max_length=30 ,default='0')
    subject1=models.CharField(max_length=30, default='0')
    marks1=models.CharField(max_length=30, default='0')
    pdf1=models.FileField(null=True , blank=True)
    subject2=models.CharField(max_length=30, default='0')
    marks2=models.CharField(max_length=30, default='0')
    pdf2=models.FileField( null=True , blank=True)
    subject3=models.CharField(max_length=30, default='0')
    marks3=models.CharField(max_length=30, default='0')
    pdf3=models.FileField(null=True , blank=True)
    subject4=models.CharField(max_length=30, default='0')
    marks4=models.CharField(max_length=30, default='0')
    pdf4=models.FileField(null=True , blank=True)
    subject5=models.CharField(max_length=30, default='0')
    marks5=models.CharField(max_length=30, default='0')
    pdf5=models.FileField( null=True , blank=True)
    Total=models.CharField(max_length=30, default='0')
    res=models.CharField(max_length=30 , default='0')

    def __str__(self):
       return str(self.enrollment_no)
    

class notice_board(models.Model):
    notice=models.TextField(default="NO notice to show")