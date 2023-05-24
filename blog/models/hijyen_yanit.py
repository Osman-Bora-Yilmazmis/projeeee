from django.db import models
from blog.models.gorevli import GorevliModel
from autoslug import AutoSlugField
from blog.abstract_models import TalepFormuAbstractModel

class HijyenYanitModel(GorevliModel):
    gorevli_sayi = models.IntegerField(null=True)
    hijyen_aciklama = models.TextField(blank=True,null=True)
    class Meta:
        db_table = 'hijyen_yanit'
        verbose_name_plural = 'Hijyen Yanıt Formları'
        verbose_name = 'Hijyen Yanıt Formu'

    def __str__(self): #admin panelinde isim olarak görünmesi için
        return self.gorevli_isim_soyisim