from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from  django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

class Category(models.Model):
    img=models.ImageField(upload_to="category")
    title=models.CharField(max_length=255)
    publish=models.DateTimeField(default=timezone.now)   

    
    def __str__ (self):
        return self.title
    
class Post (models.Model):
    title=models.CharField(max_length=300)
    price=models.PositiveIntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    img=models.ImageField(upload_to="post")
    # img=models.FileField(blank=True,upload_to="post")
    # cove=SimpleUploadedFile(img,b"post/")
    model_post=models.CharField(max_length=300)
    cpu=models.CharField(max_length=300)
    ram=models.CharField(max_length=300)
    hard=models.CharField(max_length=300)
    gpu=models.CharField(max_length=300,default="...")
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(max_length=250,unique_for_date="publish")
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    update=models.DateTimeField(auto_now=True)
    publish=models.DateTimeField(default=timezone.now)
    
    
     
    def __str__ (self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post:postdetail",args=[self.slug,self.id ])
        


class ImagSlid(models.Model):
    img=models.ImageField(upload_to="slid")
    publish=models.DateTimeField(default=timezone.now)
   
    