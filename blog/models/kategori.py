from django.db import models
from autoslug import AutoSlugField

class KategoriModel(models.Model):
    isim = models.CharField(max_length=30, blank=False, null=False)
    slug = AutoSlugField(populate_from='isim', unique=True)

    class Meta:
        db_table = 'kategori'
        verbose_name_plural = 'kategoriler'
        verbose_name = 'kategori'

    def __str__(self) -> str: #admin panelinde isim olarak görünmesi için
        return self.isim