from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
User=get_user_model()
class RegisterForm(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',"placeholder": 'Confirm Password'}),validators=[validate_password])
    class Meta:
        model=User
        fields=("first_name", "last_name", "email","username","password")
        widgets={
          "first_name": forms.TextInput(attrs={'class': 'form-control',"placeholder": "First Name",}),
          "last_name": forms.TextInput(attrs={'class': 'form-control',"placeholder": "Last Name",}),
          "email": forms.EmailInput(attrs={'class': 'form-control',"placeholder": "Email",}),
          "username": forms.TextInput(attrs={'class': 'form-control',"placeholder":"Username",}),
          "password": forms.PasswordInput(attrs={'class': 'form-control',"placeholder": "Password"},),
                }
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if confirm_password != None:
         if password != confirm_password:
           if self._errors.get('confirm_password')!=None:
            self._errors['confirm_password'].append('Password not equal')
           else:
               self._errors['confirm_password']=[]
               self._errors['confirm_password'].append("Password not equal")
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',"placeholder": 'Password'}))
