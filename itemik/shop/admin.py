from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models
# Register your models here.

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Goods)
admin.site.register(models.Tag)
