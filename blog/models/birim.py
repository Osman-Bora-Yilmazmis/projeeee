from django.db import models
from autoslug import AutoSlugField

class BirimModel(models.Model):
    birim = models.CharField(max_length=30, blank=False, null=False)
    slug = AutoSlugField(populate_from='birim', unique=True)

    class Meta:
        db_table = 'birim'
        verbose_name_plural = 'birimler'
        verbose_name = 'birim'

    def __str__(self) -> str: #admin panelinde isim olarak görünmesi için
        return self.birim