from django import forms
from blog.models import HijyenYanitModel

class HijyenYanit(forms.ModelForm):

    class Meta:
        model = HijyenYanitModel
        fields = ( 
            'hijyen_aciklama', 'gorevli_isim_soyisim'
        )