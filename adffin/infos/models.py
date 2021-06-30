from django.db import models
from django.utils import timezone

# Create your models here.

class news(models.Model):
    author=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    description=models.TextField()
    fun_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.author

class newsdate(models.Model):
    author=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    description=models.TextField()
    fun_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.author

class RegistrationData(models.Model):
    name=models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class InfoData(models.Model):
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.DateField(max_length=20)
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.CharField(max_length=10)
    qualification = models.CharField(max_length=30)
    salary = models.IntegerField(default=100)
    pan = models.CharField(max_length=100)
    req_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.fname

class Response(models.Model):
    req_id = models.IntegerField()
    response = models.CharField(max_length=200)
    reason = models.CharField(max_length=500)

    def __str__(self):
        return self.req_id



