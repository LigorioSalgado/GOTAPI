from django.db import models

# Create your models here.
class place (models.Model):

	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	description = models.TextField()
	continent = models.CharField(max_length=10,choices=(('WT','Westeros'),('ES','Essos'),('OH','Other')))
	religion = models.CharField(max_length=50)