from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EmployeeDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empcode = models.CharField(max_length=10)
    empdept = models.CharField(max_length=50,null=True)
    designation = models.CharField(max_length=100,null=True)
    salary = models.IntegerField(null=True)
    contact = models.IntegerField(null=True)
    gender = models.CharField(max_length=10,null=True)
    joiningdate = models.DateField(null=True)
    # name = models.CharField(max_length=50)
    # email = models.EmailField(max_length=50)
    # pwd = models.CharField(max_length=50)
    # cpwd = models.CharField(max_length=50)
    def __str__(self):
        return self.user.username
