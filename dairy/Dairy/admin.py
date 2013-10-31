from django.contrib import admin
from Dairy.models import Farmer,Animal,Milk

class MilkInline(admin.TabularInline):
	model=Milk
	extra=2
class AnimalInline(admin.TabularInline):
	model=Animal
	extra=2
class FarmerAdmin(admin.ModelAdmin):
	fields=['farmer_name','farmer_address','farmer_id','join_date']
	
	inlines=[AnimalInline]

admin.site.register(Farmer,FarmerAdmin)
