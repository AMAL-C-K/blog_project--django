from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body1 = models.TextField()
    body2 = models.TextField(blank=True)
    body3 = models.TextField(blank=True)
    subtitle1 = models.CharField(max_length=200, blank=True)
    subtitle2 = models.CharField(max_length=200, blank=True)
    cover_image = models.ImageField()
    created_on = models.DateTimeField(auto_now_add=True)
