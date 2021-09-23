from django.db import models
from data_tags.slug_generator import unique_slug_generator
from django.db.models.signals import pre_save,post_save
from products.models import Porduct


#6.6
#tag
#tag mode
# Create your models here.
class Tag(models.Model):
   title       = models.CharField(max_length=100)
   slug        = models.SlugField()
   timestamps  = models.DateTimeField(auto_now_add=True)
   active      = models.BooleanField(default=True)
   product     = models.ManyToManyField(Porduct,blank=True)



def tag_pre_save_reciver(sender,instance,*args,**kwargs):
   if not instance.slug:
      instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_reciver,sender=Tag)