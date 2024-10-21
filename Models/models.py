from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

DEPARTMENT_CHOICES = [
    ('SCMCS', 'SCMCS'),
    ('SNAHS', 'SNAHS'),
    ('SMLS', 'SMLS'),
    ('SITHM', 'SITHM'),
    ('SASE', 'SASE'),
]

PROGRAM_CHOICES = [
    ('ABCOM', 'ABCOM'),
    ('ABMMA', 'ABMMA'),
    ('AHM', 'AHM'),
    ('BACOMM', 'BACOMM'),
    ('BARNCII', 'BARNCII'),
    ('BEED', 'BEED'),
    ('BMMA', 'BMMA'),
    ('BPP NCII', 'BPP NCII'),
    ('BSA', 'BSA'),
    ('BSAIS', 'BSAIS'),
    ('BSAT', 'BSAT'),
    ('BSB', 'BSB'),
    ('BSBA', 'BSBA'),
    ('BSC', 'BSC'),
    ('BSCS', 'BSCS'),
    ('BSE', 'BSE'),
    ('BSED', 'BSED'),
    ('BSHM', 'BSHM'),
    ('BSHRM', 'BSHRM'),
    ('BSIT', 'BSIT'),
    ('BSIT(TEST)', 'BSIT(TEST)'),
    ('BSMLS', 'BSMLS'),
    ('BSMT', 'BSMT'),
    ('BSN', 'BSN'),
    ('BSN (YIBU)', 'BSN (YIBU)'),
    ('BSNED', 'BSNED'),
    ('BSOT', 'BSOT'),
    ('BSP', 'BSP'),
    ('BSPSY', 'BSPSY'),
    ('BSPT', 'BSPT'),
    ('BSPT (YIBU)', 'BSPT (YIBU)'),
    ('BSRT', 'BSRT'),
    ('BSRT (YIBU)', 'BSRT (YIBU)'),
    ('BSTM', 'BSTM'),
    ('BSTRM', 'BSTRM'),
    ('CCNCII', 'CCNCII'),
    ('CCPIII-TAFE', 'CCPIII-TAFE'),
    ('CGNCII', 'CGNCII'),
    ('CGNCII (T)', 'CGNCII (T)'),
    ('CHSNCII', 'CHSNCII'),
    ('CTP', 'CTP'),
    ('DB', 'DB'),
    ('DBM-KENT', 'DBM-KENT'),
    ('DM', 'DM'),
    ('DMM-KENT', 'DMM-KENT'),
    ('EIMNCII', 'EIMNCII'),
    ('FBSNCII', 'FBSNCII'),
    ('FL', 'FL'),
    ('HSKNCII', 'HSKNCII'),
    ('MAP', 'MAP'),
    ('MAP (YIBU)', 'MAP (YIBU)'),
    ('MBA', 'MBA'),
    ('MBA (YIBU)', 'MBA (YIBU)'),
    ('MD', 'MD'),
    ('MD(TEST)', 'MD(TEST)'),
    ('MISICT', 'MISICT'),
    ('MSN', 'MSN'),
    ('PNCIV', 'PNCIV'),
    ('PRE-DENT', 'PRE-DENT'),
    ('SMAWNCI', 'SMAWNCI'),
    ('SMAWNCII', 'SMAWNCII'),
    ('VACOMLIT', 'VACOMLIT'),
    ('WSA', 'WSA'),
]

CURRICULUM_YEAR_CHOICES = [
        ('2016-2017', '2016-2017'),
        ('2017-2018', '2017-2018'),
        ('2018-2019', '2018-2019'),
        ('2019-2020', '2019-2020'),
        ('2020-2021', '2020-2021'),
        ('2021-2022', '2021-2022'),
        ('2022-2023', '2022-2023'),
        ('2023-2024', '2023-2024'),
        ('2024-2025', '2024-2025'),
    ]

STUDENT_STATUS_CHOICES = [ 
    ('Enrolled', 'Enrolled'),
    ('Graduated', 'Graduated'),
    ('Dropped', 'Dropped'),
    ('Transferred', 'Transferred'),
    ('Failed', 'Failed'),
    ('Incomplete', 'Incomplete'),
]
class Account(AbstractUser):
    department = models.CharField(max_length=32, choices=DEPARTMENT_CHOICES, default='SCMCS')

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
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Curriculum(models.Model):
    year = models.CharField(max_length=32, choices=CURRICULUM_YEAR_CHOICES, unique=True)
    program = models.CharField(max_length=32, choices=PROGRAM_CHOICES)
    data = models.JSONField()

    def __str__(self):
        return self.year