from django.db import models
from django.contrib.auth.models import AbstractUser
from Models.utils.choices import DEPARTMENT_CHOICES, PROGRAM_CHOICES, CURRICULUM_YEAR_CHOICES, STUDENT_STATUS_CHOICES, CATEGORY_CHOICES, ROLE_CHOICES
from Models.utils.directory_helper import get_program_highlight_directory, get_article_media_directory, get_announcement_media_directory


class Account(AbstractUser):
    program = models.CharField(max_length=64, choices=PROGRAM_CHOICES, default='BSIT', blank=True, null=True) 
    department = models.CharField(max_length=32, choices=DEPARTMENT_CHOICES, default='SCMCS')
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default='Student')

    def __str__(self):
        return self.username

class Student(models.Model):
    
    name = models.CharField(max_length=100)
    student_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    course_status = models.JSONField(blank=True, null=True)
    curriculum_year = models.CharField(max_length=100, choices=CURRICULUM_YEAR_CHOICES, default='2024-2025')
    program = models.CharField(max_length=64, choices=PROGRAM_CHOICES, default='BSIT')
    student_status = models.CharField(max_length=100, default='Enrolled', choices = STUDENT_STATUS_CHOICES)

    def save(self, *args, **kwargs):
        # Check if the instance already exists in the database
        if self.pk:
            # Get the current instance from the database
            current_instance = Student.objects.get(pk=self.pk)
            self.check_graduation_status()

        super(Student, self).save(*args, **kwargs)
        
        
        
    def check_graduation_status(self):
        # Check if all the subjects in the curriculum have been passed
        if all(status.lower() == 'passed' for status in self.course_status.values()):
            self.student_status = 'Graduated'
        elif any(status.lower() == 'failed' for status in self.course_status.values()):
            self.student_status = 'Failed'
        elif any(status.lower() == 'incomplete' for status in self.course_status.values()):
            self.student_status = 'Incomplete'
        else:
            self.student_status = 'Enrolled'
    


    
    def __str__(self):
        return self.name






class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    image = models.ImageField(upload_to=get_article_media_directory, blank=True, null=True, default='default.jpg')
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.CharField(max_length=256, choices = CATEGORY_CHOICES, default='General')
    date = models.DateTimeField(auto_now_add=True)
    department = models.CharField(max_length=32, choices=DEPARTMENT_CHOICES, default='SCMCS')   
    program = models.CharField(max_length=64, choices=PROGRAM_CHOICES, default='BSIT')

    def __str__(self):
        return f"{self.title} - {self.author}"
    
    
class ProgramHighlight(models.Model):
    department = models.CharField(max_length=32, choices=DEPARTMENT_CHOICES, default='SCMCS')   
    program = models.CharField(max_length=64, choices=PROGRAM_CHOICES, default='BSIT')
    image = models.ImageField(upload_to=get_program_highlight_directory, blank=True, null=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return f"{self.title} - {self.program}"
    
    


class Curriculum(models.Model):
    year = models.CharField(max_length=32, choices=CURRICULUM_YEAR_CHOICES, unique=True)
    program = models.CharField(max_length=32, choices=PROGRAM_CHOICES)
    data = models.JSONField()

    def __str__(self):
        return f"{self.program} - {self.year}"