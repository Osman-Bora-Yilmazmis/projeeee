from django.db import models
from autoslug import AutoSlugField

class MalzemeModel(models.Model):
    malzeme_adi = models.CharField(max_length=50, blank=False, null=False)
    malzeme_adedi = models.IntegerField()
    #form_kategori = models.ForeignKey(FormKategoriModel, related_name='malzeme_kategorileri', on_delete=models.CASCADE)
    class Meta:
        db_table = 'malzeme'
        verbose_name_plural = 'Malzemeler'
        verbose_name = 'Malzeme'

    def __str__(self): #admin panelinde isim olarak görünmesi için
        return self.malzeme_adi