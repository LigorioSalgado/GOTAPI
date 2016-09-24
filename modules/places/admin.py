from django.contrib import admin
from .models import place
# Register your models here.
class PlaceAdmin(admin.ModelAdmin):
	pass


admin.site.register(place,PlaceAdmin)