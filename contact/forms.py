from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Форма подписки по email"""
    

   

    class Meta:
        
            model = Contact
            fields = ("first_name","email" )
            widgets = {
                "first_name": forms.TextInput(attrs={"class": "editContent", "placeholder": "Name..."}),

                "email": forms.TextInput(attrs={"class": "editContent", "placeholder": "Your Email..."})
                
            }
            labels = {
                "email": '',
                "first_name": ''
            }

