from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager

# Create your models here.


class User(AbstractUser):
    def __str__(self):
        return self.username


class SocialCard(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='SocialCards', null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    front_message = models.TextField(max_length=300, blank=True, null=True)
    back_message = models.TextField(max_length=300, blank=True, null=True)
    front_image = models.URLField(blank=True, null=True)
    back_image = models.URLField(blank=True, null=True)
    font = models.CharField(max_length=50, null=True, blank=True)
    text_color = models.CharField(max_length=50, null=True, blank=True)
    border_color = models.CharField(max_length=50, null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return f'{self.title}'


class Follower(models.Model):
    pass
