#tekrar eden modeller için tablo oluşturmayan soyut bir dosya
from django.db import models

class DateAbstractModel(models.Model):
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class TalepFormuAbstractModel(models.Model):
    baslik = models.CharField(max_length=50 ,blank=True,null=True)
    aciklama = models.TextField(blank=True,null=True)
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True)
    MY_CHOICES = [('Onay Bekliyor', 'Onay Bekliyor'), 
                  ('Onaylandı', 'Onaylandı'), ('Reddedildi', 'Reddedildi'), 
                  ('İşlem Yapılıyor', 'İşlem Yapılıyor')]
    islem_durumu = models.CharField(max_length=50, choices=MY_CHOICES, default='Onay Bekliyor')

    idari_calisanlar = [('Pınar Hanım', 'Pınar Hanım'), 
                  ('Bahar Hanım', 'Bahar Hanım')]
    idari_calisan = models.CharField(max_length=50, choices=idari_calisanlar, null = True)
    
    class Meta:
        abstract = True


class RolAbstractModel(models.Model):
    isim = models.CharField(max_length=100, blank=True,null=True)
    soyisim = models.CharField(max_length=100, blank=True,null=True)
    tel_no = models.CharField(max_length=11,blank=True,null=True)
    email = models.EmailField(unique=True)
    sifre = models.CharField(max_length=50,blank=False,null=False)

    class Meta:
        abstract = True
