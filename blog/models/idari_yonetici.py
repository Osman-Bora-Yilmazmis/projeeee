from django.db import models
from blog.models.birim import BirimModel
from account.models import CustomUserModel
from blog.abstract_models import RolAbstractModel

class İdariYoneticiModel(RolAbstractModel):

    # user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    calistigi_birim = models.ForeignKey(BirimModel, on_delete=models.CASCADE, related_name='yonetici_birimi')

    class Meta:
        db_table = 'idari_yonetici'
        verbose_name_plural = 'İdari Birim Yöneticisi'
        verbose_name = 'İdari Birim Yöneticisi'

    def __str__(self): #admin panelinde isim olarak görünmesi için
        return self.isim_soyisim
    
