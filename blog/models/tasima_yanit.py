from django.db import models
from blog.models.gorevli import GorevliModel
from autoslug import AutoSlugField
from blog.abstract_models import TalepFormuAbstractModel
from blog.models.kategori import KategoriModel

class TasimaYanitModel(GorevliModel):
    aciklama = models.TextField(blank=True,null=True)
    class Meta:
        db_table = 'tasima_yanit'
        verbose_name_plural = 'Taşıma Yanıt Formları'
        verbose_name = 'Taşıma Yanıt Formu'

    def __str__(self): #admin panelinde isim olarak görünmesi için
        return self.gorevli_isim_soyisim