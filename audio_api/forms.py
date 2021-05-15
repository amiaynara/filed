from django import forms
from django.forms import ModelForm

from .models import Podcast

class PodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = '__all__' 
