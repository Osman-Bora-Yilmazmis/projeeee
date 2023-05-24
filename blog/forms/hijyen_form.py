from django import forms

from blog.models import HijyenModel

class HijyenForm(forms.ModelForm):
    class Meta:
        model = HijyenModel
        fields = ('baslik', 'aciklama')