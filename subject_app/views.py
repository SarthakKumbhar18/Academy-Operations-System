from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import *
# Create your views here.

def subject_list_view(request): 
    data = Subject.objects.all()
    # print(data)
    context = {"data":data}
    return render(request,"subject_app/subject_list.html",context)

def subject_info_view(request,subject_name):
    obj = get_object_or_404(Subject, Name=subject_name)
    # print(obj)
    return render(request,"subject_app/subject_info.html",{"data":obj})


