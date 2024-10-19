from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)  
    student_number = models.CharField(max_length=100) 
    email = models.EmailField(max_length=100, blank = True, null = True) 
    phone_number = models.CharField(max_length=100, blank = True, null = True)
    address = models.CharField(max_length=100, blank = True, null = True)
    course_status = models.JSONField(blank = True, null = True)
    curriculum_year = models.CharField(max_length=100, blank = True, null = True)
    

    def __str__(self):
        return self.name