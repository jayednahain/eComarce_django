from django.db import models
from django.db.models import Q


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
             Q(price__icontains=query)
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
