from django.contrib import admin
from blog.models import KategoriModel
from blog.models import YazilarModel
from blog.models import YorumModel
from blog.models import IletisimModel
from blog.models import MalzemeModel
from blog.models import SarfMalzemeModel
from blog.models import GorevliModel
from blog.models import HijyenModel
from blog.models import TasimaModel
from blog.models import DepartmanModel
from blog.models import SunCalisanModel
from blog.models import İdariCalisanModel
from blog.models import İdariYoneticiModel
from blog.models import BirimModel
from blog.models import SarfMalzemeYanitModel
from blog.models import HijyenYanitModel
from blog.models import TasimaYanitModel


# Register your models here.
@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik', 'icerik')
    list_display = (
        'baslik', 'olusturulma_tarihi','düzenlenme_tarihi'
    )
@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    list_display = ('yazan', 'olusturulma_tarihi','guncellenme_tarihi')
    search_fields = ('yazan_username',)

@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    list_display = ('email', 'olusturulma_tarihi')
    search_fields = ('email',)

admin.site.register(KategoriModel)

@admin.register(MalzemeModel)
class MalzemeAdmin(admin.ModelAdmin):
    list_display = ('malzeme_adi' , 'malzeme_adedi')
    search_fields = ('malzeme_adi',)

@admin.register(SarfMalzemeModel)
class SarfMalzemeAdmin(admin.ModelAdmin):
    list_display = ('baslik' , 'sarf_malzeme_adi','olusturulma_tarihi')
    search_fields = ('sarf_malzeme_adi',)

@admin.register(GorevliModel)
class GorevliAdmin(admin.ModelAdmin):
    list_display = ('gorevli_isim_soyisim' ,)
    search_fields = ('gorevli_isim_soyisim',)

@admin.register(HijyenModel)
class HijyenAdmin(admin.ModelAdmin):
    list_display = ('baslik','olusturulma_tarihi')
    search_fields = ('baslik',)

@admin.register(TasimaModel)
class TasimaAdmin(admin.ModelAdmin):
    list_display = ('baslik','olusturulma_tarihi')
    search_fields = ('baslik',)    

@admin.register(DepartmanModel)
class DepartmanAdmin(admin.ModelAdmin):
    list_display = ('departman_adi' ,)
    search_fields = ('departman_adi',)

@admin.register(SunCalisanModel)
class SunCalisamAdmin(admin.ModelAdmin):
    list_display = ('isim','soyisim' ,'departman',)
    search_fields = ('isim','soyisim' 'departman',) #admin sayfasında searchte hata geliyor

@admin.register(İdariCalisanModel)
class İdariCalisanAdmin(admin.ModelAdmin):
    list_display = ('isim','soyisim', 'calistigi_birim',)
    search_fields = ('isim','soyisim', 'calistigi_birim',)

@admin.register(BirimModel)
class BirimAdmin(admin.ModelAdmin):
    list_display = ('birim',)
    search_fields = ('birim',)

@admin.register(İdariYoneticiModel)
class İdariYoneticiAdmin(admin.ModelAdmin):
    list_display = ('isim','soyisim')
    search_fields = ('isim','soyisim')

@admin.register(SarfMalzemeYanitModel)
class SarfMalzemeYanitAdmin(admin.ModelAdmin):
    list_display = ('malzeme_adi',)
    search_fields = ('malzeme_adi',)

@admin.register(HijyenYanitModel)
class HijyenYanitAdmin(admin.ModelAdmin):
    list_display = ('gorevli_isim_soyisim',)
    search_fields = ('gorevli_isim_soyisim',)

@admin.register(TasimaYanitModel)
class TasimaYanitAdmin(admin.ModelAdmin):
    list_display = ('gorevli_isim_soyisim',)
    search_fields = ('gorevli_isim_soyisim',)

