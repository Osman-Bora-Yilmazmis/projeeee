from django.db import models

class DepartmanModel(models.Model):
    departman_adi = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        db_table = 'departman'
        verbose_name_plural = 'Departmanlar'
        verbose_name = 'Departman'

    def __str__(self): #admin panelinde isim olarak görünmesi için
        return self.departman_adi