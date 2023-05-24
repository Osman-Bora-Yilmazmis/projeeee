from django.db import models
from blog.models.malzeme import MalzemeModel
from autoslug import AutoSlugField
from blog.abstract_models import TalepFormuAbstractModel
from blog.models.gorevli import GorevliModel
from account.models import CustomUserModel

class HijyenModel(TalepFormuAbstractModel):
    
    gorevli_kisi =  models.ForeignKey(GorevliModel, on_delete=models.CASCADE, related_name='hijyen_gorevli_kisi',null = True)
    slug = AutoSlugField(populate_from = 'baslik', unique=True, null = True, blank=True, allow_unicode=True)
    idari_calisanlar = [('Pınar Hanım', 'Pınar Hanım'), 
                  ('Bahar Hanım', 'Bahar Hanım')]
    idari_calisan = models.CharField(max_length=50, choices=idari_calisanlar, null = True, default='Pınar Hanım')
    kategori_adi = models.CharField(max_length=50,  null = True, default='Hijyen')
    form_gonderen = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='hijyen_formlar',null = True)
    class Meta:
        db_table = 'hijyen'
        verbose_name_plural = 'Hijyen Formları'
        verbose_name = 'Hijyen Formu'

    def __str__(self): #admin panelinde isim olarak görünmesi için
        return self.baslik