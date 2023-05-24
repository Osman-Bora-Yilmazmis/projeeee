from django.db import models
from blog.models.malzeme import MalzemeModel
from autoslug import AutoSlugField
from blog.abstract_models import TalepFormuAbstractModel
from blog.models.kategori import KategoriModel

class SarfMalzemeYanitModel(MalzemeModel):
    aciklama = models.TextField(blank=True,null=True)
    class Meta:
        db_table = 'sarf_malzeme_yanit'
        verbose_name_plural = 'Sarf Malzeme Yanıt Formları'
        verbose_name = 'Sarf Malzeme Yanıt Formu'

    def __str__(self): #admin panelinde isim olarak görünmesi için
        return self.malzeme_adi