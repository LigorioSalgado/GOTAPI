from django.contrib import admin
from .models import  Castle

class CastleAdmin(admin.ModelAdmin):
	pass


admin.site.register(Castle,CastleAdmin)
