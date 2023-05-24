from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class CustomUserModel(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/',blank=True,null=True,) #blank ve null(db'de) boş kalabilmesi için
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11,blank=True,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    class Meta():
        db_table = 'user'
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Kullanıcılar'
    
    def __str__(self) -> str:
        return self.username
    
    