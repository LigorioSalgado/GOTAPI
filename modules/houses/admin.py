from django.contrib import admin
from .models import House
class HouseAdmin(admin.ModelAdmin):
	pass


admin.site.register(House,HouseAdmin)