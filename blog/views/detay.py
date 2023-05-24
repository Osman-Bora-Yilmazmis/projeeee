from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from blog.models.hijyen_formu import HijyenModel
from blog.models.tasima_formu import TasimaModel
from blog.models.sarf_malzeme_formu import SarfMalzemeModel
from blog.models.malzeme import MalzemeModel
from blog.models.gorevli import GorevliModel
from django.http import HttpResponseForbidden

class DetayView(View):

    def get(self, request, Formslug, slug):
        model_map = {
            'hijyen': HijyenModel,
            'tasima': TasimaModel,
            'sarf-malzeme': SarfMalzemeModel,
        }

        

        Model = model_map.get(Formslug)

        form = get_object_or_404(Model, slug=slug)
        malzemeler = MalzemeModel.objects.values_list('malzeme_adi', flat=True).distinct()
        gorevliler = GorevliModel.objects.values_list('gorevli_isim_soyisim', flat=True).distinct()

        return render(request, 'pages/detay.html', context={
            'form': form,
            'malzemeler': malzemeler,
            'gorevliler': gorevliler
        })

    def post(self, request, Formslug, slug):
        model_map = {
            'hijyen': HijyenModel,
            'tasima': TasimaModel,
            'sarf-malzeme': SarfMalzemeModel,
        }

        

        Model = model_map.get(Formslug)

        form = get_object_or_404(Model, slug=slug)
        malzemeler = MalzemeModel.objects.values_list('malzeme_adi', flat=True).distinct()
        gorevliler = GorevliModel.objects.values_list('gorevli_isim_soyisim', flat=True).distinct()

        if 'guncelle' in request.POST:
            aciklama = request.POST.get('aciklama')
            form.aciklama  = aciklama
            if(Formslug == "sarf-malzeme"):

                sarf_malzeme_adi = request.POST.get('sarf_malzeme_adi')
                sarf_malzeme_adedi = request.POST.get('sarf_malzeme_adedi')
                malzeme = MalzemeModel.objects.get(malzeme_adi=sarf_malzeme_adi)
                form.sarf_malzeme_adi  = malzeme
                form.sarf_malzeme_adedi  = sarf_malzeme_adedi

            form.save()
        elif 'sil' in request.POST:
            form.delete()
            return redirect('liste')
        
        elif 'onayla' in request.POST:
                islem_durumu = request.POST.get('islem_durumu')
                form.islem_durumu = 'Onaylandı'
                form.save()
        
        elif 'reddet' in request.POST: #HEPSİ ICIN ORTAK
                islem_durumu = request.POST.get('islem_durumu')
                form.islem_durumu = 'Reddedildi'
                form.save()
        
        elif 'gorev_ata' in request.POST:
            if Formslug == "hijyen" or Formslug == 'tasima':
                
                gorevli_kisi = request.POST.get('gorevli_kisi')
                print(gorevli_kisi)
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")
                islem_durumu = request.POST.get('islem_durumu')
                form.islem_durumu = 'İşlem Yapılıyor'
                gorevli = GorevliModel.objects.get(gorevli_isim_soyisim=gorevli_kisi)
                         
                form.gorevli_kisi = gorevli          
                form.save()

        return render(request, 'pages/detay.html', context={
            'form': form,
            'malzemeler': malzemeler,
            'gorevliler': gorevliler
        })
