from django.db import models

# Create your models here.

class Book (models.Model):

	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=80)
	autor = models.CharField(max_length=40,default="George R.R. Martin", blank=True)
	date_published = models.DateField()
	num_pages = models.IntegerField()
	isbn = models.CharField(max_length=80)

	def __str__(self):
		return 'Book: ' + self.name
