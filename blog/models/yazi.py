from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModel

class YazilarModel (models.Model):
    resim = models.ImageField(upload_to='yazi_resimleri')
    baslik = models.CharField(max_length=50)
    icerik = RichTextField()
    slug = AutoSlugField(populate_from = 'baslik', unique=True)
    kategoriler = models.ManyToManyField(KategoriModel, related_name='yazi') 
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    düzenlenme_tarihi = models.DateTimeField(auto_now=True)
    #ManytoMany bir yazının birden fazla kategoriye atanması için
    #related_name bir kategorideki tüm yazıları görebilmek için
    yazar = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE,related_name='yazilar')
    #on_delete eğer yazar silinirse yazıları da silinir

    class Meta:
        verbose_name = 'Yazi'
        verbose_name_plural = 'Yazilar'
        db_table = 'Yazi'

    def __str__(self):
        return self.baslik