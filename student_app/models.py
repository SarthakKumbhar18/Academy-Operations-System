from django.db import models

# Create your models here.

class Student(models.Model):
    Student_Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    Course = models.CharField(max_length=30)
    Dob = models.DateField()
    Emailid = models.EmailField()
    username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "Student" 

    