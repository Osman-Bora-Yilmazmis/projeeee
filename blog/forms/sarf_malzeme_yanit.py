from django import forms
from blog.models import SarfMalzemeModel

class SarfYanit(forms.ModelForm):

    class Meta:
        model = SarfMalzemeModel
        fields = ( 
            'sarf_aciklama', 'form_gonderen'
        )