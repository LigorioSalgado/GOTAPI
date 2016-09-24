from django.db import models
#from modules.characters.models import Character
from modules.castles.models import Castle
from modules.books.models import Book
# Create your models here.

class House(models.Model):

	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=80)
	castle = models.ForeignKey(Castle,on_delete=models.CASCADE,null=True,blank=True)
	history = models.TextField()
	words = models.CharField(max_length=150, null=True, blank=True)
	coat_of_arms = models.TextField()
	#current_lord = models.OneToOneField(Character)
	books = models.ManyToManyField(Book)
	house_image = models.ImageField(upload_to='houses/',null=True,blank=True)

	def __str__(self):
		return 'House ' + self.name