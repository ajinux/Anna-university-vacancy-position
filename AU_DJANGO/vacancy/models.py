# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class College(models.Model):
    name = models.CharField(max_length=512)
    counselling_code = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=512)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Caste(models.Model):
    name = models.CharField(max_length=255)
    total_seats = models.IntegerField()

    def __unicode__(self):
        return self.name


class CollegeDepartment(models.Model):
    college = models.ForeignKey(College, related_name='departments')
    department = models.ForeignKey(Department, related_name='Colleges')


class SeatsRemaining(models.Model):
    clg_dept = models.ForeignKey(CollegeDepartment, related_name='clg_dept_seats')
    caste = models.ForeignKey(Caste, related_name='caste_seats')
    seats_remaining = models.IntegerField()
    recorded_at = models.DateTimeField()
