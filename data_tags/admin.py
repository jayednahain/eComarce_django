from django.contrib import admin
from data_tags.models import Tag


# Register your models here.
class TagAdmin(admin.ModelAdmin):
   list_display = ['__str__','slug'] #we want to show the slug field with strig format !
   class Meta:
      model = Tag


admin.site.register(Tag,TagAdmin)