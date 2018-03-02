from django.db import models

# Create your models here.

class Reagent(models.Model):

    name = models.CharField(max_length=100)
    mw = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
