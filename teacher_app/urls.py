
from django.urls import path
from .views import *
urlpatterns = [
    path('teacher_home/',teacher_home_view,name="teacher_home"),
    path('teacher_signup/', teacher_signup_view, name="teacher_signup"),
    path('teacher_signin/', teacher_signin_view, name="teacher_signin"),
    path('teacher_dashboard/<int:id>/', teacher_dashboard_view, name="teacher_dashboard"),
    path('teacher_attandence/<str:subjects>/', teacher_attandence_view, name="teacher_attandence"),
    path('teacher_signout/', teacher_signout_view, name="teacher_signout"),
]
