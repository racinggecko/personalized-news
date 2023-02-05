from django.contrib.auth.models import User
from django.db import models

class NewsSource(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribed_sources = models.ManyToManyField(NewsSource)
    interests = models.TextField()

    def __str__(self):
        return self.user.username
