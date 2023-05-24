from django.db import models

class GorevliModel(models.Model):
    gorevli_isim_soyisim = models.CharField(max_length=100,blank=True, null=True)

    class Meta:
        db_table = 'gorevli'
        verbose_name_plural = 'Görevliler'
        verbose_name = 'Görevli'

    def __str__(self): #admin panelinde isim olarak görünmesi için
        return self.gorevli_isim_soyisim