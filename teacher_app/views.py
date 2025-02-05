from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from subject_app.models import *
from student_app.models import *
# Create your views here.

def teacher_home_view(request):
    return render(request,"teacher_app/teacher_home.html")


def teacher_signup_view(request):
    if(request.method == "POST"):
        print(request.POST)
        id = request.POST.get("tid")
        name = request.POST.get("tname")
        sub = request.POST.get("sub")
        eml = request.POST.get("email")
        un = request.POST.get("uname")
        pd = request.POST.get("pwd")
        print(id,name,sub,eml,un,pd)
        if(User.objects.filter(username=un).exists()):
            print("User already exists")
            messages.error(request, "Username already taken. Please choose another.")
            return render(request,'teacher_app/teacher_signup.html',{'error':'Username or email already exist'})
        else:
            User.objects.create_user(username = un,email=eml,password=pd )
            print("User created Successfully")
            obj = Teacher.objects.create(Teacher_Id=id,T_Name=name,Subject=sub,Email_ID=eml,Username=un,Password=pd)
            obj.save()
            return redirect("teacher_signin")


    return render(request,"teacher_app/teacher_signup.html")

def teacher_signin_view(request):
    if (request.method == "POST"):
        print(request.POST)
        id = request.POST.get("tid")
        un = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        # print(id,un,pwd)
        try :
            obj = Teacher.objects.get(Teacher_Id=id)
            if (obj.Username == un and obj.Password == pwd):
                user = authenticate(request,username=un, password=pwd)
                if user is not None:
                    login(request, user)
                    return redirect("teacher_dashboard",id)
                else:
                    messages.error(request, "Invalid credentials") 
        except Teacher.DoesNotExist:
            messages.error(request, 'Teacher ID not found')
    
    return render(request,"teacher_app/teacher_signin.html")


@login_required
def teacher_dashboard_view(request,id):
    obj = Teacher.objects.get(Teacher_Id = id)
    print(obj.Subject)

    return render(request,"teacher_app/teacher_dashboard.html",{"subjects":obj.Subject})
@login_required
def teacher_attandence_view(request,subjects):
    if(request.method == "POST"):
        print(request.POST)
    
    print(subjects)
    subject = Subject.objects.get(Name=subjects)
    students = Student.objects.all() 

    return render(request,"teacher_app/teacher_attandence.html",{"students":students,"subjects":subject})

# @login_required
def teacher_signout_view(request):
     logout(request)
     return redirect("teacher_home")



  







  