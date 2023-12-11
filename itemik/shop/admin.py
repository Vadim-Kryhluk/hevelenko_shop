from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models

# Register your models here.

class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'price', 'photo', 'is_published']
    list_display_links = ('name', 'price')
    search_fields = ('name', 'category')

    def description(self, obj):
        return obj.description[:50]


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Goods, GoodsAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Profile)
