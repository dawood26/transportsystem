from django import forms
from . import  models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CreateDepartment(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = ['name','description','code']

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email','phone','address')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email','phone','address')