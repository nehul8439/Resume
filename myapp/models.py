from django.db import models

# Create your models here.
class Resume(models.Model):
	fullname=models.CharField(max_length=20,blank=True)
	phone=models.CharField(max_length=20,blank=True)
	mail=models.EmailField(max_length=30,blank=True)
	message=models.CharField(max_length=20,blank=True)
	class Meta:
		db_table='resume'
