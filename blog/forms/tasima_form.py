from django import forms
from blog.models import TasimaModel

class TasimaForm(forms.ModelForm):

    class Meta:
        model = TasimaModel
        fields = ('baslik', 'aciklama')