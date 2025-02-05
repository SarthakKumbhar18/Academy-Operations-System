from django.urls import path
from .views import *
urlpatterns = [
    path('student_home/', student_home_view,name="student_home"),
    path('student_signup/', student_signup_view,name="student_signup"),
    path('student_signin/', student_signin_view,name="student_signin"),
    path('student_details/<int:s_id>/', student_details_view,name="student_details"),
    path('student_edit/<int:s_id>/',student_edit_view,name="student_edit"),
    
]