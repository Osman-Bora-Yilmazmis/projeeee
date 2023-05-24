from django import forms
from blog.models import TasimaYanitModel

class TasimaYanit(forms.ModelForm):

    class Meta:
        model = TasimaYanitModel
        fields = ( 
            'aciklama', 'gorevli_isim_soyisim'
        )