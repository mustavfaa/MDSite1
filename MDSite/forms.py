from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

from django import forms







class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']


class UploadDocumentForm(forms.Form):
	
    file = forms.FileField()
    image = forms.ImageField()



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']





class CommentForm(forms.ModelForm):
	content=forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control','placeholder':'text goes here!!!' , 'rows':'2', 'cols' : '50'}))
	class Meta:
		model=Comment
		fields=('content',)