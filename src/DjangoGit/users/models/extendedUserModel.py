from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class GitProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=60, blank=True)
    token_type = models.CharField(max_length=30, blank=True)
    scope = models.CharField(max_length=50, blank=True)
    git_username = models.CharField(max_length=100, blank=True)
    git_id = models.IntegerField(blank=True, null=True)

@receiver(post_save, sender=User)
def create_user_git_profile(sender, instance, created, **kwargs):
    if created:
        GitProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.gitprofile.save()
