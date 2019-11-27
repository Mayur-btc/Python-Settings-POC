from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm


class UserCreateForm(ModelForm):
    class Meta:
        model = User
        fields = ['phone_number', 'gender', 'birthday', 'birth_location', 'image']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({
                'placeholder': 'Name',
                'class': 'input-calss_name'
            })

