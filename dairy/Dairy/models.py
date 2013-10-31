from django.db import models

class Farmer(models.Model):
	farmer_name=models.CharField(max_length=200)
	farmer_address=models.CharField(max_length=1000)
	farmer_id=models.IntegerField(default=0)
	join_date=models.DateTimeField("join_date")
	def __unicode__(self):
	  return self.farmer_name
class Animal(models.Model):
	animal_type=models.CharField(max_length=20)
	number_animals=models.IntegerField(default=0)
	animal_insurance=models.CharField(max_length=20)
	insurance_amount=models.IntegerField(default=0)
	insurance_date=models.DateTimeField("insurance_date")
	farmer=models.ForeignKey(Farmer)
	def __unicode__(self):
	  return self.animal_type
class Milk(models.Model):
	milk_quantity=models.CharField(max_length=20)
	milk_fat=models.IntegerField(default=0)
	milk_lr=models.IntegerField(default=0)
	milk_rate=models.IntegerField(default=0)
	animal=models.ForeignKey(Animal)
	def __unicode__(self):
	  return self.milk_quantity	

# Create your models here.
