from django.db import models
from random import randint 

# Create your models here.

class User(models.Model):
	firstname= models.TextField(max_length=50)
	lastname = models.TextField(max_length=50)
	# May need to set a default value
	status = models.TextField(max_length=12)
	
	def create_status(self):
		'''Random to determine status.'''
		rando = randint(1, 10)
		if rando % 2 == 0:
			self.status = 'GRANTED'
		else:
			self.status = 'DENIED' 
	
	def __str__(self):
		fullname = self.firstname + ' ' + self.lastname 
		return fullname.title()
		
