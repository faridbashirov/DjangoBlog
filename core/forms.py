from django import forms

from .models import Contact

    
    
    
class ContactForm(forms.ModelForm):
    class Meta:
     model=Contact
     fields="__all__"
     widgets={
         "name":forms.TextInput(attrs={'class':'form-control name mb-4' ,
               "placeholder": 'full name',"id":"name"}),
         "email":forms.EmailInput(attrs={'class': 'form-control email mb-4',
               "placeholder": 'Email',"id":"Email"}),
         'subject':forms.TextInput(attrs={'class': 'form-control subject mb-4',
               "placeholder": 'subject',"id":"subject"}),
         "message":forms.TextInput(attrs={'class': 'form-control message mb-4',
               "placeholder": 'Write your comment',"id":"message"}),
         
     }