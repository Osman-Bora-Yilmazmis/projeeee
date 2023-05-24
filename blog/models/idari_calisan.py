from django.db import models
from blog.models.birim import BirimModel
from blog.abstract_models import RolAbstractModel

class İdariCalisanModel(RolAbstractModel):

    calistigi_birim = models.ForeignKey(BirimModel, on_delete=models.CASCADE, related_name='idari_calisan_birimi')

    class Meta:
        db_table = 'idari_birim_calisan'
        verbose_name_plural = 'İdari Birim Çalışanları'
        verbose_name = 'İdari Birim Çalışanı'



    def __str__(self): #admin panelinde isim olarak görünmesi için
        return self.isim_soyisim
    
    