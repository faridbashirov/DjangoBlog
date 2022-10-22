from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from core.models import AbstractModel
from django.contrib.auth import get_user_model

User=get_user_model()
class Category(AbstractModel):
    title=models.CharField(max_length=150)
    def __str__(self):
        return self.title
  
class BlogList(AbstractModel):
    title= models.CharField(max_length=150)
    image=models.ImageField(upload_to="static/media/images/")
    short_description=models.TextField(max_length=100)
    long_description=models.TextField( )
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category,related_name='categories')
   

class Comments(AbstractModel):
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=255 )
    message=models.TextField(max_length=255 )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blogs=models.ForeignKey(BlogList,on_delete=models.CASCADE)
       
    
    
