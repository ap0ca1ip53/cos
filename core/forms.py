__author__ = 'ap0ca1ip53'
from django import forms
from models import OS
from django.contrib.auth.models import User


class OSForm(forms.ModelForm):

    class Meta:
        model = OS
        fields = ['']

    def save(self, commit=True):
