from django import forms
from .models import newsModel

class newsForms(forms.ModelForm):
    #required degani bu biz admin panelda malumot to`ldirishimiz majbur degani false qilsak uni to'ldirmasak ham bo'ladi
    # name_uz = forms.CharField(required=True)
    # name_en = forms.CharField(required=False)
    name_uz = forms.CharField(required=True)
    name_en = forms.CharField(required=False)
    name_ru = forms.CharField()

    text_uz = forms.CharField()
    text_en = forms.CharField()
    text_ru = forms.CharField()


    class Meta:
        model = newsModel
        exclude = ['name', 'text']