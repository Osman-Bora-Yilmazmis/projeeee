from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator #Sayfalama işlemi için gereken paginator kütüphanesini aktifleştirmemizi sağlar
from django.contrib.auth.decorators import login_required #login olmadan yazılarım sayfasını açmaya çalışırlarsa bu kütüphane yardımcı olucak
from django.db.models import Q
from itertools import chain

@login_required(login_url='/') #eğer login olmadan yazılarım sayfasını görüntülemek isterse otomatikman anasayfaya yönlendirilir
def formlarim(request):
    
    sorgu = request.GET.get('sorgu')
    hijyen_formlarim = request.user.hijyen_formlar.order_by("-id") #siteye giren userin yazilarini azalan id ye göre sıralar (buradaki yazilar related namedir user.yazilar diyerek kullanıcının bütün yazılarına erişebilmiş olduk)
    tasima_formlarim = request.user.tasima_formlar.order_by("-id")
    sarf_formlarim = request.user.sarf_formlar.order_by("-id")

    if(sorgu):
        hijyen_formlarim = hijyen_formlarim.filter(
            Q(baslik__icontains=sorgu) |
            Q(islem_durumu__icontains=sorgu) |
            Q(olusturulma_tarihi__icontains=sorgu) |
            Q(idari_calisan__icontains=sorgu) |
            Q(kategori_adi__icontains=sorgu)
        ).distinct()    
        sarf_formlarim = sarf_formlarim.filter(
            Q(baslik__icontains=sorgu) |
            Q(islem_durumu__icontains=sorgu) |
            Q(olusturulma_tarihi__icontains=sorgu) |
            Q(idari_calisan__icontains=sorgu) |
            Q(kategori_adi__icontains=sorgu)
        ).distinct()
        tasima_formlarim = tasima_formlarim.filter(
            Q(baslik__icontains=sorgu) |
            Q(islem_durumu__icontains=sorgu) |
            Q(olusturulma_tarihi__icontains=sorgu) |
            Q(idari_calisan__icontains=sorgu) |
            Q(kategori_adi__icontains=sorgu)
        ).distinct()
    sayfa = request.GET.get('sayfa') #bir istek sırasında belirli bir parametrenin değerini almak için kullanılır.
    yazilarim = list(
            sorted(
                chain(hijyen_formlarim,tasima_formlarim,sarf_formlarim),
                key=lambda objects: objects.olusturulma_tarihi,
                reverse=True  # Optional
            ))
    paginator = Paginator(yazilarim , 10) #yazilar 2'li 2'li şekilde sıralanır 

    return render(request, 'pages/formlarim.html', context = {
        'yazilarim': paginator.get_page(sayfa),
    })