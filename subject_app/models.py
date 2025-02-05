from django.db import models

# Create your models here.
class Subject(models.Model):
    Name = models.CharField(max_length=30)
    Trainer = models.CharField(max_length=30)
    Duration = models.IntegerField()
    Syllabus = models.CharField(max_length=100)
    Fees = models.FloatField()

    def __str__(self):
        return self.Name
    
    class Meta:
        db_table = "Subject"

    