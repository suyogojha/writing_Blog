from django.db import models
import uuid
from django.utils import timezone
from datetime import datetime
from ckeditor.fields import RichTextField 
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify
from writer.models import Profile

# Create your models here.
class Post(models.Model):
    writer = models.ForeignKey(Profile, on_delete = models.SET_NULL, null = True, blank = True)
    title = models.CharField(max_length=500)
    image  = models.ImageField(upload_to='img', default='img/default.jpg')
    body = RichTextField()
    slug = models.SlugField(unique=True)
    post_id = models.UUIDField(default = uuid.uuid4, unique=True, editable = False, primary_key = True)
    tag = models.ForeignKey('Tag', on_delete = models.SET_NULL, blank = True, null = True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length = 500)
    slug = models.SlugField()
    tag_id = models.UUIDField(default = uuid.uuid4, unique=True, editable = False, primary_key = True)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    id = models.UUIDField(default = uuid.uuid4, unique=True, editable = False, primary_key = True)

    def __str__(self):
        return self.body