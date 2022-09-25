from django.db import models
from datetime import datetime


class Post(models.Model):
    author = models.CharField(max_length=40, null=False)
    title = models.CharField(max_length=50, null=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    content = models.TextField(null=False)
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

class Comments(models.Model):
    comment_author = models.CharField(max_length=30)
    comment_body = models.CharField(max_length=200, null=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    post = models.ForeignKey('Post', on_delete= models.CASCADE)

    def __str__(self):
        return self.comment_author

