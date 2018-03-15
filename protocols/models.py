

from datetime import date
from django.db import models


TIME_UNITS_CHOICES = (("  s","s"),
                      ("min","min"),
                      ("  h","h"),
                      ("  d","y"))

SPEED_UNITS_CHOICES = (("  g","  g"),
                       ("rpm","rpm"))

TEMPERATURE_UNITS_CHOICES = (("C","C"),
                             ("F","F"))

VOLUME_UNITS_CHOICES = (("uL","uL"),
                        ("mL","mL"),
                        (" L"," L"))

class Protocol(models.Model):

    CHOICES = (
        ('---','-----'),
        ('Mix', 'Mix'),
        ('Inc', 'Incubate'),
        ('Cen', 'Centrifuge'),
        ('Dec', 'Decant'),
        ('Trm', 'Thermocylce'),
        ('Rsp', 'Resuspend'),
        ('Tns', 'Transfer'),
        ('Opr', 'Operate'))

    date_range = models.CharField(max_length=15,default='',null=True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)


class Step(models.Model):

    protocol = models.ForeignKey(Protocol, on_delete=models.CASCADE,default=None)


    CHOICES = (
        ('-----','-----'),
        ('Mix', 'Mix'),
        ('Incubate', 'Incubate'),
        ('Centrifuge', 'Centrifuge'),
        ('Decant', 'Decant'),
        ('Thermocycle', 'Thermocycle'),
        ('Resuspend', 'Resuspend'),
        ('Transfer', 'Transfer'),
        ('Operate', 'Operate'))


    # common features
    name        = models.CharField(max_length=255,choices=CHOICES,default='-----')
    preamble    = models.CharField(max_length=20,default='')
    postamble   = models.CharField(max_length=20,default='')
    # step features
    # MIX
    reagents = models.CharField(max_length=15,default='',null=True)
    temperature = models.CharField(max_length=15,default='',null=True)
    temperature_units = models.CharField(max_length=4,choices=TEMPERATURE_UNITS_CHOICES,default='C')
    # INCUBATE
    time = models.FloatField(default=1)
    time_units = models.CharField(max_length=3,choices=TIME_UNITS_CHOICES,default='min')
    temperature = models.FloatField(default=23)
    temperature_units = models.CharField(max_length=4,choices=TEMPERATURE_UNITS_CHOICES,default='C')
    # CENTRIFUGE
    speed = models.FloatField(default=8000)
    speed_units = models.CharField(max_length=3,choices=SPEED_UNITS_CHOICES,default='  g')
    temperature = models.FloatField(default=23)
    temperature_units = models.CharField(max_length=4,choices=TEMPERATURE_UNITS_CHOICES,default='C')
    

class ThermocycleStep(models.Model):

    CHOICES = (
            ('----','----'),
            ('Hold','Hold'),
            ('Goto','Goto')
            )

    step = models.ForeignKey(Step, on_delete=models.CASCADE,default=None)

    stage_type = models.CharField(max_length=4,choices=CHOICES,default='Hold',null=True)
    goto_step = models.IntegerField(default=1)
    repeats = models.IntegerField(default=1)
    stage_temp = models.FloatField(default=23)
    stage_temp_units = models.CharField(max_length=4,choices=TEMPERATURE_UNITS_CHOICES,default='C')
    stage_time = models.FloatField(default=1)
    stage_time_units = models.CharField(max_length=3,choices=TIME_UNITS_CHOICES,default='min')







