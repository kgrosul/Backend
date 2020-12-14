from django.db import models


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


class Test(models.Model):
    name = models.CharField(max_length=100)
    add_info = models.TextField(max_length=500)


class Question(models.Model):
    question = models.CharField(max_length=200)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    answers = models.JSONField()


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    comment = models.TextField(default=None)
    timestamp = models.DateTimeField()




