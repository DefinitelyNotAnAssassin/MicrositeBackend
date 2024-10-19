from django.urls import path 
from API import views 


urlpatterns = [ 
               path('students', views.get_students, name='get_students'),
               path('students/<str:student_number>', views.get_student, name='get_student'),
               path('setCurriculumStatus', views.set_curriculum_status, name='set_curriculum_status'),
               ]