from django.db import models


class AbstractModel(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True
        
class Contact(AbstractModel):
    name = models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    subject=models.CharField(max_length=255)
    message=models.TextField(max_length=255)
    
    def __str__(self):
        return self.name
class About(AbstractModel):
    description=models.TextField()
    large_image= models.ImageField(upload_to="static/media/About")
    image=models.ImageField(upload_to="static/media/About")
    
    