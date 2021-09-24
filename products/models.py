from django.db import models

#9
#image path
from products.media_path_converter import upload_image_path
# from products.manager import ProductManager
#12
#signal
from django.db.models.signals import pre_save,post_save

#12
#slug generator function
from products.slug_generator import unique_slug_generator
from django.urls import reverse
from django.db import models
from django.db.models import Q



#11 7:45
#creating custmon queryset model!

class ProductQuerySet(models.query.QuerySet):
   def featured_new(self):
      return self.filter(featured=True)



#Manager
#creating manager for Product
#this manager will retrive data by id
#10



class ProductQuerySet(models.query.QuerySet):
   def active(self):
      return self.filter(active=True)

   def featured(self):
      return self.filter(featured=True,active=True)

   #search
   #custom query
   def search_data(self,query):
      query_set = (
             Q(title__icontains=query) |
             Q(description__icontains=query) |
             Q(price__icontains=query) |
             Q(tag__title__icontains=query) # this is a revarce query

      )

      return self.filter(query_set).distinct()


class ProductManager(models.Manager):

   # 11 overide get_queryset() method
   def get_queryset(self):
      return ProductQuerySet(self.model, using=self._db)


   def get_by_id(self,id): #create method
      #return self.get_queryset(id=id)
      #3:28
      qs = self.get_queryset().filter(id=id) #get_queryset() built in method !
      if qs.count()==1: # it must return one value
         return qs.first()
      return None


   #11 nakeing query for featured product
   def featured(self):
      return self.get_queryset().featured() #return those value where featured=True


   #search
   #adding custom search_data() to manader
   def search_data(self,query):
      return self.get_queryset().search_data(query)



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
   date           = models.DateTimeField(auto_now_add=True)


   def __str__(self):
      return str(self.title)

   def slug_product_link(self):
      return reverse("CB_slug_deatil",kwargs={"slug":self.slug})

   # def get_absolute_url(self):
   #    return "/product/product_slug_detail_CB/{slug}/".format(slug=self.slug)

#12
#signal
#this signal will create when any one create any product
#this signal will generate slug !
def product_pre_save_reciver(sender,instance,*args,**kwargs):
   if not instance.slug:
      instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_reciver,sender=Porduct)