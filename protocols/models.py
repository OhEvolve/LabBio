

from datetime import date
from django.db import models

from reagents.models import Liquid,Solid,Biologic


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

DECANT_ACTION_CHOICES = (('-------','-----'),
                         ('Discard','Discard'),
                         ('  Save ','Save'))

VOLUME_UNITS_CHOICES = (("uL","uL"),
                        ("mL","mL"),
                        (" L"," L"))


MASS_UNITS_CHOICES = (("ng/L","ng/L"),
                      ("ug/L","ug/L"),
                      ("mg/L","mg/L"),
                      (" g/L"," g/L"),
                      (" nM "," nM "),
                      (" uM "," uM "),
                      (" mM "," mM "),
                      ("  M ","  M "))

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
    # DECANT 
    action = models.CharField(default='-------',max_length=7,choices=DECANT_ACTION_CHOICES)
    # THERMOCYCLE
    # (none,iterable)
    # RESUSPEND 
    liquids   = models.ManyToManyField(Liquid,through='AddedLiquid',symmetrical=False)
    solids    = models.ManyToManyField(Solid,through='AddedSolid',symmetrical=False)
    biologics = models.ManyToManyField(Biologic,through='AddedBiologic',symmetrical=False)
    # reagnets,filler,total
    # TRANSFER 
    container = models.CharField(default='1.5mL Tube',max_length=30)
    # OPERATE
    # (none,iterable)


class OperateStep(models.Model):

    step = models.ForeignKey(Step, on_delete=models.CASCADE,default=None)
    description = models.CharField(max_length=255)
    

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

""" Reagent listing through models """


class AddedLiquid(models.Model):
    reagent  = models.ForeignKey(Liquid,on_delete=models.CASCADE) # may be wrong on_delete behavior
    step = models.ForeignKey(Step,on_delete=models.CASCADE) # may be wrong on_delete behavior
    volume       = models.FloatField(default=1)
    volume_units = models.CharField(max_length=2,choices=VOLUME_UNITS_CHOICES,default=' L')

class AddedSolid(models.Model):
    reagent  = models.ForeignKey(Solid,on_delete=models.CASCADE) # may be wrong on_delete behavior
    step = models.ForeignKey(Step,on_delete=models.CASCADE) # may be wrong on_delete behavior
    mass       = models.FloatField(default=0)
    mass_units = models.CharField(max_length=4,choices=MASS_UNITS_CHOICES,default=' g/L')
            
class AddedBiologic(models.Model):
    reagent  = models.ForeignKey(Biologic,on_delete=models.CASCADE) # may be wrong on_delete behavior
    step = models.ForeignKey(Step,on_delete=models.CASCADE) # may be wrong on_delete behavior
    mass       = models.FloatField(default=0)
    mass_units = models.CharField(max_length=4,choices=MASS_UNITS_CHOICES,default=' g/L')







