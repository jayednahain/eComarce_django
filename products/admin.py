from django.contrib import admin

# Register your models here.

from .models import Porduct


class ProductAdmin(admin.ModelAdmin):
   list_display = ['__str__','slug'] #we want to show the slug field with strig format !
   class Meta:
      model = Porduct


admin.site.register(Porduct,ProductAdmin)
