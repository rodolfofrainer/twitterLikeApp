import random

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("TweetsModel", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class TweetsModel(models.Model):
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name = 'tweet_user', blank=True, through=TweetLike)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-id']
    
    @property
    def is_retweet(self):
        return self.parent != None