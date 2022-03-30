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
