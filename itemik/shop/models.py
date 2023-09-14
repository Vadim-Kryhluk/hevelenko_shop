from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey('self',
                            related_name="children",
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True
                            )

    class MPTTMeta:
        order_insertion_by = ['name', 'slug', 'parent']

    class Meta:
        verbose_name = "Категорії"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name




class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = "Теги"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name

class Goods(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва товару')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото товару')
    description = models.TextField(blank=True, verbose_name='Опис товару')
    price = models.CharField(max_length=20, blank=True, verbose_name="Ціна товару")
    category = models.ForeignKey(Category,
                                 related_name="post",
                                 on_delete=models.SET_NULL,
                                 null=True
                                 )
    tags = models.ManyToManyField(Tag, related_name="post")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товари"
        verbose_name_plural = "Товари"



