from django.db import models

# Create your models here.

class Creature (models.Model):

	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=80)
	appearance = models.TextField()
	history = models.TextField()
	is_extint = models.BooleanField(default=False)
	image = models.ImageField(upload_to='creatures/', null=True,blank=True)