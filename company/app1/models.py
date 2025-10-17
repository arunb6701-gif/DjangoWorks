from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    designation=models.CharField(max_length=100)
    salary=models.IntegerField()
    image=models.ImageField(upload_to="image")