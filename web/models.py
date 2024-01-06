from django.db import models
from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField

from django.urls import reverse_lazy
# Create your models here.

class Service(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True, max_length=100)
    image=VersatileImageField(upload_to='services')
    description=HTMLField()

    def get_absolute_url(self):
        return reverse_lazy('web:service-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
    
    
    
    
class Blog(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True, max_length=200)
    date=models.DateField(blank=True, null=True)
    image=VersatileImageField(upload_to='blogs')
    description=HTMLField()
    
    def get_absolute_url(self):
        return reverse_lazy('web:blog-detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title
    
    
class Testmonial(models.Model):
    name=models.CharField(max_length=200)
    position=models.CharField(max_length=200,blank=True, null=True)
    description=models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Faq(models.Model):
    question=models.CharField(max_length=200)
    answer=models.TextField()
    
    def __str__(self):
        return self.question
    
    
class PortfolioCategory(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Portfolio(models.Model):
    category=models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)
    subtitle=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    image=VersatileImageField(upload_to='portfolio')
    
    
    def __str__(self):
        return self.title
    
    
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.TextField()

    def str(self):
        return self.name
    
class Client_logo(models.Model):
    image=VersatileImageField(upload_to='client_logo')
    
    def __str__(self):
        return str(self.image)