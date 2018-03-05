
'''
Models for the reagents app
'''

# library imports
from django.db import models


SEQUENCE_FORM_CHOICES = (("p",     "plasmid"),
                         ("l",     "genomic"),
                         ("r", "recombinant"))
                         
SEQUENCE_SHAPE_CHOICES = (("c",   "circular"),
                          ("l",     "linear"))

SEQUENCE_MATERIAL_CHOICES = (("dD",       "dsDNA"),
                             ("sD",       "ssDNA"),
                             ("dR",       "dsRNA"),
                             ("sR",       "ssRNA"),
                             ("pp",     "protein"))                          

class Matter(models.Model):
	""" Matter reference object (base class) """
	name = models.CharField(max_length=255)
	owner = models.CharField(max_length=255,blank=True)
    
	def __str__(self):
		return '{} - {}'.format(type(self).__name__,self.name)

class Liquid(Matter):
	
	""" Liquid reference object """
	
	pass
	
	
class Solid(Matter):
	
	""" Solid reference object """
	
	mw = models.CharField(max_length=20)
	
	
class Biologic(Matter):
   	
   """ Sequence codon"""
   
   sequence = models.TextField(max_length=10000)
   form = models.CharField(max_length = 1,choices = SEQUENCE_FORM_CHOICES)
   shape = models.CharField(max_length = 1,choices = SEQUENCE_SHAPE_CHOICES)
   material = models.CharField(max_length = 2,choices = SEQUENCE_MATERIAL_CHOICES)
                  		   
                  		   
                  	   
class Solution(Matter):
	
	""" Liquid reference object """
	
	pass
                  		   
                  		   
            
