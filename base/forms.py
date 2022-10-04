from django.forms import ModelForm
from django import forms
from .models import Pharms


class PharmForm(ModelForm):

    class Meta:
        model = Pharms
        fields = '__all__'
        #fields = ('name', 'description', 'localisation', 'commune')
