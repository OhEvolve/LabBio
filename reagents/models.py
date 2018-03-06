
'''
Models for the reagents app
'''

# library imports
from django.db import models
from django.forms import ModelMultipleChoiceField


SEQUENCE_FORM_CHOICES = (("  plasmid  ",     "plasmid"),
                         ("  genomic  ",     "genomic"),
                         ("recombinant", "recombinant"))
                         
SEQUENCE_SHAPE_CHOICES = (("circular",   "circular"),
                          (" linear ",     "linear"))

SEQUENCE_MATERIAL_CHOICES = ((" dsDNA ",       "dsDNA"),
                             (" ssDNA ",       "ssDNA"),
                             (" dsRNA ",       "dsRNA"),
                             (" ssRNA ",       "ssRNA"),
                             ("protein",     "protein"))                          

SOLUTION_CONTENT_CHOICES = ((" liquid "," liquid "),
                            ("  solid ","  solid "),
                            ("biologic","biologic"))



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
   form = models.CharField(max_length = 11,choices = SEQUENCE_FORM_CHOICES)
   shape = models.CharField(max_length = 8,choices = SEQUENCE_SHAPE_CHOICES)
   material = models.CharField(max_length = 7,choices = SEQUENCE_MATERIAL_CHOICES)
                  		   

                  		   
class Solution(Matter):
        
    """ Liquid reference object """

    #liquids   = models.ForeignKey(Liquid,  on_delete=models.SET_NULL, null=True)
    liquids   = models.ManyToManyField(Liquid,through='Contains')

    #solids    = models.ForeignKey(Solid,   on_delete=models.SET_NULL, null=True)
    #biologics = models.ForeignKey(Biologic,on_delete=models.SET_NULL, null=True)
    #solutions = models.ForeignKey("self",  on_delete=models.SET_NULL, null=True)
                  		   

class Contains(models.Model):
    reagent  = models.ForeignKey(Liquid,on_delete=models.DO_NOTHING) # may be wrong on_delete behavior
    solution = models.ForeignKey(Solution,on_delete=models.DO_NOTHING) # may be wrong on_delete behavior
    volume = models.CharField(max_length=16)
                  		   
            
