from django.db import models
import os
import random
# Create your models here.

#formating image file name
#8
def get_filename(filepath):
   base_name      = os.path.basename(filepath)
   name,extension = os.path.splitext(base_name)
   return name,extension


def upload_image_path(instance,filename):

   new_filename   = random.randint(1,34545465)
   name,extension = get_filename(filename)
   final_filename = f'{new_filename}{extension}'.format(new_filename=new_filename,extension=extension)
   return f'Porduct_image/{new_filename}/{final_filename}'.format(
      new_filename=new_filename,
      final_filename=final_filename
   )


class Porduct(models.Model):
   title          = models.CharField(max_length=120)
   description    = models.TextField()
   price          = models.DecimalField(decimal_places=2,max_digits=20,default=00.00)
   product_image  = models.ImageField(upload_to=upload_image_path,null=True,blank=True)


   def __str__(self):
      return str(self.title)
