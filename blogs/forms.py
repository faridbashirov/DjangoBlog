from django import forms
from .models import Category, Comments,BlogList

class CommentForm(forms.ModelForm):
    class Meta:
     model=Comments
     fields=["name","email","message"]
     widgets={
         "name":forms.TextInput(attrs={'class':'form-control name mb-4' ,
               "placeholder": 'full name',"id":"name"}),
         "email":forms.EmailInput(attrs={'class': 'form-control email mb-4',
               "placeholder": 'Email',"id":"Email"}),
         "message":forms.TextInput(attrs={'class': 'form-control message mb-4',
               "placeholder": 'Write your comment',"id":"message"}),
         
     }

class AddBlogForm(forms.ModelForm):
      class Meta:
       model=BlogList
       fields=["title","image","short_description","long_description","categories"]
       widgets={
            "title":forms.TextInput(attrs={'class':'form-control title mb-4',
            "placeholder":'Blog title',"id":"title"}),
            "image":forms.FileInput(attrs={'class':'form-control image mb-4',"id":"image"}),
            "short_description":forms.TextInput(attrs={'class':'form-control desc mb-4',
            "placeholder":'Short Description',"id":"desc1"}),
            "long_description":forms.Textarea(attrs={'class':'form-control desc mb-4',
            "placeholder":'Long Description',"id":"desc"}),
             
       }
       categories = forms.ModelMultipleChoiceField( queryset=Category.objects.all(),widget=forms.CheckboxSelectMultiple)
           