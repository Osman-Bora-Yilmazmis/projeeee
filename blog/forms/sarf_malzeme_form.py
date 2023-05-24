from django import forms
from blog.models import SarfMalzemeModel

class SarfMalzemeForm(forms.ModelForm):

    class Meta:
        model = SarfMalzemeModel
        fields = ('baslik', 'aciklama','sarf_malzeme_adi', 'sarf_malzeme_adedi')