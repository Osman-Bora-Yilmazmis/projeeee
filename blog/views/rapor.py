from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseForbidden
from blog.models import HijyenModel, SarfMalzemeModel, TasimaModel

@login_required
def rapor(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Bu sayfaya erişmek için yetkiniz yok.")

    idari_calisan = "Pınar Hanım"
    islem_durumlari = ['Onay Bekliyor', 'Onaylandı', 'Reddedildi', 'İşlem Yapılıyor']
    form_turleri = ['Hijyen','Taşıma','Sarf Malzeme']
    
    pinar_veri_sayilari = []
    bahar_veri_sayilari = []
    pinar_form_sayilari = []
    bahar_form_sayilari = []
    
    #PINAR HANIM İÇİN İŞLEM DURUMLARI GRAFİGİNİN VERİLERİ
    for durum in islem_durumlari:
        count = sum(
            [
                model.objects.filter(idari_calisan=idari_calisan, islem_durumu=durum).count()
                for model in [HijyenModel, TasimaModel, SarfMalzemeModel]
            ]
        )
        pinar_veri_sayilari.append((count))
    pinar_toplam_veri = sum(pinar_veri_sayilari)

    #PINAR HANIM İÇİN FORM SAYILARI GRAFİGİNİN VERİLERİ
    for form in form_turleri:
        count = sum(
            [
                model.objects.filter(idari_calisan=idari_calisan, kategori_adi=form).count()
                for model in [HijyenModel, TasimaModel, SarfMalzemeModel]
            ]
        )
        pinar_form_sayilari.append((count))
    
    #BAHAR HANIM İÇİN İŞLEM DURUMLARI GRAFİGİNİN VERİLERİ
    idari_calisan = "Bahar Hanım"
    for durum in islem_durumlari:
        count = sum(
            [
                model.objects.filter(idari_calisan=idari_calisan, islem_durumu=durum).count()
                for model in [HijyenModel, TasimaModel, SarfMalzemeModel]
            ]
        )
        bahar_veri_sayilari.append((count))
    bahar_toplam_veri = sum(bahar_veri_sayilari)

    #BAHAR HANIM İÇİN FORM SAYILARI GRAFİGİNİN VERİLERİ
    for form in form_turleri:
        count = sum(
            [
                model.objects.filter(idari_calisan=idari_calisan, kategori_adi=form).count()
                for model in [HijyenModel, TasimaModel, SarfMalzemeModel]
            ]
        )
        bahar_form_sayilari.append((count))
    


    return render(request, 'pages/rapor.html',{
        'pinar_veri_sayilari': pinar_veri_sayilari,
        'bahar_veri_sayilari': bahar_veri_sayilari,
        'pinar_toplam_veri':pinar_toplam_veri,
        'bahar_toplam_veri':bahar_toplam_veri,
        'pinar_form_sayilari':pinar_form_sayilari,
        'bahar_form_sayilari':bahar_form_sayilari,
    })