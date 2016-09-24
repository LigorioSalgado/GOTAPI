from django.db import models
#from modules.houses.models import House
from modules.books.models import Book
from modules.houses.models import House
# Create your models here.


class Character(models.Model):

	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=60)
	biography = models.TextField()
	description = models.TextField()
	house = models.ForeignKey(House,null=True,blank=True,related_name='members')
	gender = models.CharField(max_length=10,choices=(('ML','Male'),('FM','Female')))
	birth_year = models.CharField(max_length=20,null=True,blank=True)
	books = models.ManyToManyField(Book)
	is_dead = models.BooleanField(default=False)

	

	def __str__(self):
		return self.name
