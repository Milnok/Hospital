from django.contrib.auth.models import User
from django.db import models


class Doctor(User):
    class Meta:
        verbose_name = "doctor"

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Patient(User):
    age = models.PositiveSmallIntegerField('age')

    class Meta:
        verbose_name = "patient"

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Note(models.Model):
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    description = models.TextField('description', max_length=1000)
    active = models.BooleanField('active', default=True)


class Audit(models.Model):
    table = models.CharField('table', max_length=100)
    action = models.CharField('action', max_length=100)
    user = models.CharField('user', max_length=100)
    description = models.TextField('description', max_length=500)


class Timetable(models.Model):
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    monday_start = models.TimeField(default='12:00', null=True)
    monday_end = models.TimeField(default='15:00', null=True)
    tuesday_start = models.TimeField(default='12:00', null=True)
    tuesday_end = models.TimeField(default='15:00', null=True)
    wednesday_start = models.TimeField(default='12:00', null=True)
    wednesday_end = models.TimeField(default='15:00', null=True)
    thursday_start = models.TimeField(default='12:00', null=True)
    thursday_end = models.TimeField(default='15:00', null=True)
    friday_start = models.TimeField(default='12:00', null=True)
    friday_end = models.TimeField(default='15:00', null=True)
