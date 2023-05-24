from django.urls import path
from blog.views import liste, profil, sarf_malzeme_form, hijyen_form,tasima_form
from blog.views import  rapor, DetayView ,formlarim, sarf_malzeme_yanit, hijyen_yanit,tasima_yanit
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from blog.views.giris import CustomLoginView
from . import views
urlpatterns = [


    path('giris/', CustomLoginView.as_view(template_name='pages/giris.html'), name='giris'),
    path('liste',liste, name='liste'),
    path('form',sarf_malzeme_form, name='sarf_malzeme_form'),
    path('profil',profil, name='profil'),
    path('', CustomLoginView.as_view(template_name='pages/giris.html'), name='giris'),
    path('sarfmalzemeformu', sarf_malzeme_form, name='sarf_malzeme_form'),
    path('hijyenformu', hijyen_form, name='hijyen_form'),
    path('tasimaformu', tasima_form, name='tasima_form'),
    path('rapor', rapor, name='rapor'),
    path('detay/<slug:Formslug>/<slug:slug>', DetayView.as_view() , name='detay'),
    path('formlarim',formlarim, name='formlarim'),
    path('sarfmalzemeyanit', sarf_malzeme_yanit, name='sarf_malzeme_yanit'),
    path('hijyenyanit', hijyen_yanit, name='hijyen_yanit'),
    path('tasimayanit', tasima_yanit, name='tasima_yanit'),
]