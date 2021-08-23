from django.db import models

# Create your models here.


class daily_transection(models.Model):
   date= models.DateField()
   customer_name = models.CharField(max_length=100)
   customer_address = models.CharField(max_length=100)
   payment_method = models.CharField(max_length=100)
   product_name = models.CharField(max_length=100)
   product_amount = models.IntegerField()
   product_price = models.FloatField()
   total_price = models.FloatField()

