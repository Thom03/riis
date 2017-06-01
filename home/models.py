from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):
	full_name = models.CharField(max_length=50)
	email = models.EmailField()
	message = models.CharField(max_length=100)	
	
	def __unicode__(self):
		return self.email



