from django.db import models
from blog.models.departman import DepartmanModel
from account.models import CustomUserModel
from blog.abstract_models import RolAbstractModel

class SunCalisanModel(RolAbstractModel):

    # user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    departman = models.ForeignKey(DepartmanModel,on_delete=models.CASCADE, related_name='departman')
    
    class Meta:
        db_table = 'sun_calisan'
        verbose_name_plural = 'Sun Şirket Çalışanları'
        verbose_name = 'Sun Şirket Çalışanı'

    def __str__(self): #admin panelinde isim olarak görünmesi için
        return self.isim_soyisim
    
