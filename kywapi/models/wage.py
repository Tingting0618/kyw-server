from django.db import models


class Wage(models.Model):

    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    salary = models.IntegerField()
    city = models.CharField(max_length=200)
    work_state = models.CharField(max_length=50)
    year = models.IntegerField()
    source = models.CharField(max_length=200)
    timestamp = models.CharField(max_length=200)