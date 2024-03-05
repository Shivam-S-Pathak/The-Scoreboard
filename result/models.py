from django.db import models

# Create your models here.
# class Student(models.Model):
#     enrollment_id=models.CharField(max_length=30)
#     name=models.CharField(max_length=30)

# class Course(models.Model):
#     name=models.CharField(max_length=30)

# class Exam(models.Model):
#     course=models.ForeignKey(Course, on_delete=models.CASCADE)
#     semester=models.IntegerField()
#     exam_type=models.CharField(max_length=30)

# class Result(models.Model):
#     student=models.ForeignKey(Student , on_delete=models.CASCADE)
#     exam = models.ForeignKey(Exam , on_delete=models.CASCADE)
#     subject1=models.CharField(max_length=30 , default='0')
#     subject2=models.CharField(max_length=30 , default='0')
#     subject3=models.CharField(max_length=30 , default='0')
#     subject4=models.CharField(max_length=30 , default='0')
#     subject5=models.CharField(max_length=30 , default='0')
#     subject6=models.CharField(max_length=30 , default='0')
#     subject7=models.CharField(max_length=30 , default='0')
#     marks_sub1=models.FloatField(default='0')
#     marks_sub2=models.FloatField(default='0')
#     marks_sub3=models.FloatField(default='0')
#     marks_sub3=models.FloatField(default='0')
#     marks_sub4=models.FloatField(default='0')
#     marks_sub5=models.FloatField(default='0')
#     marks_sub6=models.FloatField(default='0')
#     marks_sub7=models.FloatField(default='0')


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
    subject2=models.CharField(max_length=30, default='0')
    marks2=models.CharField(max_length=30, default='0')
    subject3=models.CharField(max_length=30, default='0')
    marks3=models.CharField(max_length=30, default='0')
    subject4=models.CharField(max_length=30, default='0')
    marks4=models.CharField(max_length=30, default='0')
    subject5=models.CharField(max_length=30, default='0')
    marks5=models.CharField(max_length=30, default='0')
    Total=models.CharField(max_length=30, default='0')
    res=models.CharField(max_length=30 , default='0')
    mobile=models.CharField(max_length=30 , default='0')

    def __str__(self):
       return str(self.enrollment_no)