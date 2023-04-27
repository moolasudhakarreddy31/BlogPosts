from datetime import timezone
from django.utils import timezone
import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='mediumapp_posts',on_delete=models.PROTECT)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')



    class Meta:
        ordering = ('-publish',)



    def __str__(self):
        return self.title