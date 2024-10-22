from django.urls import path 
from API import views 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [ 
               path('students', views.get_students, name='get_students'),
               path('students/<str:student_number>', views.get_student, name='get_student'),
               path('getCurriculum', views.get_curriculum, name='get_curriculum'),
               path('setCurriculumStatus', views.set_curriculum_status, name='set_curriculum_status'),
               path('getProgramData', views.get_program_data, name='get_program_data'),
               path('getYearlyPerformance', views.get_yearly_performance, name='get_yearly_performance'),
               path('getProgramHighlights', views.get_program_highlights, name='get_program_highlights'),
               path('getProgramArticles', views.get_program_articles, name='get_program_articles'),
               path('verifyAccount', views.verify_account, name='verify_account'),
               path('verifyAuth', views.verify_auth, name='verify_auth'),
               path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
               path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
            ]