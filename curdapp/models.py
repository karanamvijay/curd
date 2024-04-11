from django.db import models

# Create your models here.
class StudentData(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)
    mobile=models.IntegerField()
    mark1=models.IntegerField()
    mark2=models.IntegerField()
    mark3=models.IntegerField()
    mark4=models.IntegerField()