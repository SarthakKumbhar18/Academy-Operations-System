from django.db import models

# Create your models here.
class Teacher(models.Model):
    Teacher_Id = models.IntegerField(primary_key=True)
    T_Name = models.CharField(max_length=30)
    Subject = models.CharField(max_length=30)
    Email_ID = models.EmailField()
    Username = models.CharField(max_length=30,default="default_user")
    Password = models.CharField(max_length=30,default="default_password")

    class Meta:
        db_table = "Teacher" 

    def __str__(self):
        return self.Name