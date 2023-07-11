import random

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class TweetsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    
    class Meta:
        ordering = ['-id']
    
    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0,200),
            "image": self.image.url if self.image else None
            }