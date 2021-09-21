from django.db import models

#9
#image path
from products.media_path_converter import upload_image_path
from products.manager import ProductManager



#11 7:45
#creating custmon queryset model!

class ProductQuerySet(models.query.QuerySet):
   def featured_new(self):
      return self.filter(featured=True)




#Manager
#creating manager for Product
#this manager will retrive data by id
#10




class Porduct(models.Model):
   title          = models.CharField(max_length=120)
   description    = models.TextField()
   price          = models.DecimalField(decimal_places=2,max_digits=20,default=00.00)
   product_image  = models.ImageField(upload_to=upload_image_path,null=True,blank=True)

   #coustom manager
   objects         = ProductManager()

   #11
   featured       = models.BooleanField(default=False)

   #12
   active         = models.BooleanField(default=True)
   slug           = models.SlugField(blank=True,unique=True)


   def __str__(self):
      return str(self.title)
