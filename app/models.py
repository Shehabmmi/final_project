from django.db import models


# Create your models here.


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)


class Course(models.Model):
    # fees = models.IntegerField()
    credit_hours = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)


class Lecture(models.Model):
    date = models.DateField()
    doctorID = models.ForeignKey('users.User', on_delete=models.CASCADE)


class Attendance(models.Model):
    date = models.DateField()
