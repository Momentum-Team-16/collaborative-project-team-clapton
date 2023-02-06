from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager

# Create your models here.


class User(AbstractUser):
    def __str__(self):
        return self.username

    @property
    def followed_list(self):
        return [follower.followed for follower in self.LoggedInUser.all()]


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
    tags = TaggableManager(blank=True)

    def __str__(self):
        return f'{self.title}'


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='LoggedInUser', null=True)
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='OtherUser', null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'followed'], name='unique_follower'
            )
        ]

    def __str__(self):
        return f'{self.user} is now following {self.followed}'

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    social_card = models.ForeignKey(SocialCard, on_delete=models.CASCADE, related_name='SocialCard')
    comment = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.comment}'
