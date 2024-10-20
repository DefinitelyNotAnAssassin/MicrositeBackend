from django.db import models

# Create your models here.


class Student(models.Model):
    CURRICULUM_YEAR_CHOICES = [
        ('2016-2017', '2016-2017'),
        ('2017-2018', '2017-2018'),
        ('2018-2019', '2018-2019'),
        ('2023-2024', '2023-2024'),
        ('2024-2025', '2024-2025'),
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
   
    name = models.CharField(max_length=100)
    student_number = models.CharField(max_length=100) 
    email = models.EmailField(max_length=100, blank = True, null = True) 
    phone_number = models.CharField(max_length=100, blank = True, null = True)
    address = models.CharField(max_length=100, blank = True, null = True)
    course_status = models.JSONField(blank = True, null = True)
    curriculum_year = models.CharField(max_length=100, choices = CURRICULUM_YEAR_CHOICES, default = '2024-2025')
    program = models.CharField(max_length=64, choices = PROGRAM_CHOICES, default = 'BSIT') 

    def __str__(self):
        return self.name
    
    


class Curriculum(models.Model):
    year = models.CharField(max_length=32, choices=Student.CURRICULUM_YEAR_CHOICES, unique=True)
    program = models.CharField(max_length=32, choices=Student.PROGRAM_CHOICES)
    data = models.JSONField()

    def __str__(self):
        return self.year