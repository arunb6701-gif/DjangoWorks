import random

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Customuser(AbstractUser):
    phone=models.IntegerField(null=True)
    role=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    is_verified=models.BooleanField(default=False) # to check whether user account is verified or not
    otp=models.CharField(max_length=1,null=True) #to store otp in backend table(CustomUser)

    def generate_otp(self):
        otp=str(random.randint(1000,9999))+str(self.id)
        self.otp=otp
        self.save()