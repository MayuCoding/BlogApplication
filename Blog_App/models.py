from django.db import models
# user mixin
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# Defining the Article model
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='videos/', null=True, verbose_name="", blank=True)
    image = models.ImageField(upload_to='images/', null=True, verbose_name="")
    thumb = models.ImageField(default='default.png', blank=True)
    
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50] + '...'
    
    def pub_date_pretty(self):
        return self.date.strftime('%b %e %Y')
    
    def pub_time_pretty(self):
        return self.date.strftime('%I:%M %p')
    
    def pub_date_time_pretty(self):
        return self.date.strftime('%b %e %Y at %I:%M %p')
    

# Defining the Comment model
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def pub_date_pretty(self):
        return self.date.strftime('%b %e %Y')
    
    def pub_time_pretty(self):
        return self.date.strftime('%I:%M %p')
    
    def pub_date_time_pretty(self):
        return self.date.strftime('%b %e %Y at %I:%M %p')
    

# User model
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
    def pub_date_pretty(self):
        return self.date.strftime('%b %e %Y')
    
    def pub_time_pretty(self):
        return self.date.strftime('%I:%M %p')
    
    def pub_date_time_pretty(self):
        return self.date.strftime('%b %e %Y at %I:%M %p')
