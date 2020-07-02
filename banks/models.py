from django.db import models

# Create your models here.

class bankDetails(models.Model):
    ifsc=models.CharField(max_length=11,primary_key=True)
    bank_id=models.DecimalField(max_digits=10,decimal_places=0,blank=True)
    branch=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=1000,null=True,blank=True)
    city=models.CharField(max_length=300,null=True,blank=True)
    district=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    bank_name=models.CharField(max_length=300,null=True,blank=True)