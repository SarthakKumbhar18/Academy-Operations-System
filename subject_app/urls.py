from django.urls import path
from .views import *
# from teacher_app import urls
urlpatterns = [   
    path("",subject_list_view,name="subject_list"),
    path("subject_information/<str:subject_name>", subject_info_view, name="subject_info"),
]
