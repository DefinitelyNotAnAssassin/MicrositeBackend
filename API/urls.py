from django.urls import path 
from API import views 


urlpatterns = [ 
            path('students', views.get_students, name='get_students'),
               path('students/<str:student_number>', views.get_student, name='get_student'),
               path('getCurriculum', views.get_curriculum, name='get_curriculum'),
               path('setCurriculumStatus', views.set_curriculum_status, name='set_curriculum_status'),
               path('getProgramData', views.get_program_data, name='get_program_data'),
               path('getYearlyPerformance', views.get_yearly_performance, name='get_yearly_performance'),
            ]