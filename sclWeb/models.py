from django.db import models

# Create your models here.
class School(models.Model):
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "School"

class SchoolReg(models.Model):
    fName = models.CharField(max_length=50)
    sName = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    re_password = models.CharField(max_length=50)

    class Meta:
        db_table = "SchoolReg"