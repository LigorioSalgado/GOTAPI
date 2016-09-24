from django.db import models

# Create your models here.

class Castle (models.Model):

	id = models.AutoField(primary_key=True)
	name =  models.CharField(max_length=100)
	description = models.TextField()
	region = models.CharField(max_length=10, choices=(('NT','NORTH'),('WE',"Westerlands"),("ES","Eastlands"),("ST","SOUTH")))

	def __str__(self):
		return 'Castle: ' + self.name
	