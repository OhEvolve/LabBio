

from datetime import date
from django.db import models



class Protocol(models.Model):

    CHOICES = (
        ('Today', 'Today'),
        ('Yesterday', 'Yesterday'),
        ('Last 7 Days', 'Last 7 Days'),
        ('Last 14 Days', 'Last 14 Days'),
        ('Last 30 Days', 'Last 30 Days'),
        ('Last 60 Days', 'Last 60 Days'),
        ('Last 90 Days', 'Last 90 Days'),
        ('This Year', 'This Year'),
        ('All Time', 'All Time'),
        ('Custom', 'Custom'))

    date_range = models.CharField(max_length=15,default='')
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)


class Step(models.Model):

    protocol = models.ForeignKey(Protocol, on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=255,default='MyProtocol')

    CHOICES = (
        ('Today', 'Today'),
        ('Yesterday', 'Yesterday'),
        ('Last 7 Days', 'Last 7 Days'),
        ('Last 14 Days', 'Last 14 Days'),
        ('Last 30 Days', 'Last 30 Days'),
        ('Last 60 Days', 'Last 60 Days'),
        ('Last 90 Days', 'Last 90 Days'),
        ('This Year', 'This Year'),
        ('All Time', 'All Time'),
        ('Custom', 'Custom'))

    date_range = models.CharField(max_length=15,default='')
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)

