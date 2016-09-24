from django.contrib import admin
from .models import Creature
# Register your models here.

class CreatureAdmin(admin.ModelAdmin):
	pass


admin.site.register(Creature,CreatureAdmin)
