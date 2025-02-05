from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import *
from django.contrib import messages
# Create your views here.
def student_home_view(request):
    return render(request,"student_app/student_home.html")

def student_signup_view(request):
    if (request.method == "POST"):
        sid = request.POST.get("s_id")
        name = request.POST.get("nm")
        course = request.POST.get("crs")
        dob = request.POST.get("dob")
        eid = request.POST.get("email")
        unm = request.POST.get("unm")
        pwd = request.POST.get("pwd")
        print(sid,name,course,dob,eid,unm,pwd)
        obj = Student.objects.create(Student_Id = sid,Name=name,Course=course,Dob=dob,Emailid=eid,username=unm,Password=pwd)
        obj.save()
        return redirect("student_signin")
    return render(request,"student_app/student_signup.html")


def student_signin_view(request):
    if (request.method =="POST"):
        # print(request.POST)
        sid = request.POST.get("student_id")
        unm = request.POST.get("username")
        pwd = request.POST.get("password")
        # print(sid,unm,pwd)
        try :
            obj = Student.objects.get(Student_Id=sid)
            # print(obj)
            if (obj.username == unm and obj.Password == pwd):
                return redirect("student_details",s_id=sid)
            else:
                messages.error(request, 'Invalid username or password')
        except Student.DoesNotExist:
             messages.error(request, 'Student ID not found')
    return render(request,"student_app/student_signin.html")

def student_details_view(request,s_id):
    # print(s_id)
    try:
        obj = Student.objects.get(Student_Id=s_id)
        # print(obj)
        return render(request, "student_app/student_info.html", {"data": obj})

    except Student.DoesNotExist:
        messages.error(request, "Student not found")
        return redirect("student_signin")
    

def student_edit_view(request,s_id):
    obj = get_object_or_404(Student, Student_Id=s_id)
    if (request.method == "POST"):
        print(request.POST)
        nm = request.POST.get("name")
        crs = request.POST.get("course")
        dob = request.POST.get("dob")
        eml = request.POST.get("email")

        if (nm):
            obj.Name = nm
        if (crs):
            obj.Course = crs
        if (dob):
            obj.Dob = dob
        if (eml):
            obj.Emailid = eml
        obj.save()        

        return redirect("student_details",s_id=s_id)
        

    return render(request,"student_app/student_edit.html")