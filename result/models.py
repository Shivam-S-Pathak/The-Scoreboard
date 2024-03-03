from django.db import models

# Create your models here.
class student(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    exam=models.CharField(max_length=30)
    semester=models.CharField(max_length=30)

    def __str__(self):
        return self.username
    

class examResult(models.Model):
    subeject1=models.CharField(max_length=30)
    subeject2=models.CharField(max_length=30)
    subeject3=models.CharField(max_length=30)