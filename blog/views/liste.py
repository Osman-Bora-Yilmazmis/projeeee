from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import HijyenModel # değiştirilcek
from blog.models import SarfMalzemeModel
from blog.models import TasimaModel
from blog.models import İdariCalisanModel
from django.db.models import Q
from itertools import chain

def liste(request):

    sorgu = request.GET.get('sorgu')
    hijyen_yazilar = HijyenModel.objects.order_by("-id") 
    sarf_yazilar = SarfMalzemeModel.objects.order_by("-id")
    tasima_yazilar = TasimaModel.objects.order_by("-id")

    if(sorgu):
        hijyen_yazilar = hijyen_yazilar.filter(
            Q(baslik__icontains=sorgu) |
            Q(islem_durumu__icontains=sorgu) |
            Q(olusturulma_tarihi__icontains=sorgu) |
            Q(idari_calisan__icontains=sorgu) |
            Q(kategori_adi__icontains=sorgu)
        ).distinct()    
        sarf_yazilar = sarf_yazilar.filter(
            Q(baslik__icontains=sorgu) |
            Q(islem_durumu__icontains=sorgu) |
            Q(olusturulma_tarihi__icontains=sorgu) |
            Q(idari_calisan__icontains=sorgu) |
            Q(kategori_adi__icontains=sorgu)
        ).distinct()
        tasima_yazilar = tasima_yazilar.filter(
            Q(baslik__icontains=sorgu) |
            Q(islem_durumu__icontains=sorgu) |
            Q(olusturulma_tarihi__icontains=sorgu) |
            Q(idari_calisan__icontains=sorgu) |
            Q(kategori_adi__icontains=sorgu)
        ).distinct()
    yazilar = list(
            sorted(
                chain(hijyen_yazilar,sarf_yazilar,tasima_yazilar),
                key=lambda objects: objects.olusturulma_tarihi,
                reverse=True  # Optional
            ))
    paginator = Paginator(yazilar,10)
    sayfa = request.GET.get("sayfa")
    

    return render(
        request, 'pages/liste.html', 
        context= {'yazilar':paginator.get_page(sayfa) }

        )



