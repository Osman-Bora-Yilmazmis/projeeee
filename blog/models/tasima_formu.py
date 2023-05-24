from django.db import models
from blog.models.malzeme import MalzemeModel
from autoslug import AutoSlugField
from blog.abstract_models import TalepFormuAbstractModel
from blog.models.gorevli import GorevliModel

class TasimaModel(TalepFormuAbstractModel):
    #görevli kişi adı ve sayıyı birbirine bağlama işlemi gerekiyor.
    gorevli_kisi =  models.ForeignKey(GorevliModel, on_delete=models.CASCADE, related_name='tasima_gorevli_kisi',null = True)
    slug = AutoSlugField(populate_from = 'baslik', unique=True, null = True, blank=True, allow_unicode=True)
    idari_calisanlar = [('Pınar Hanım', 'Pınar Hanım'), 
                  ('Bahar Hanım', 'Bahar Hanım')]
    idari_calisan = models.CharField(max_length=50, choices=idari_calisanlar, null = True, default='Pınar Hanım')
    kategori_adi = models.CharField(max_length=50,  null = True, default='Taşıma')
    form_gonderen = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='tasima_formlar',null = True)
    class Meta:
        db_table = 'tasima'
        verbose_name_plural = 'Tasima Formları'
        verbose_name = 'Tasima Formu'

    def __str__(self): #admin panelinde isim olarak görünmesi için
        return self.baslik