from django.db import models
from django.utils import timezone


class Doctor(models.Model):
    name = models.CharField(max_length=55)
    surname = models.CharField(max_length=55)
    birth = models.DateField()
    add_info = models.TextField(max_length=500)


class User(models.Model):
    name = models.CharField(max_length=55)
    surname = models.CharField(max_length=55)
    birth = models.DateField()
    bio = models.TextField(max_length=500)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class DoctorUser(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Test(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=55)
    test = models.JSONField()


class Result(models.Model):
    test = models.ForeignKey(Test, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    result = models.JSONField()




