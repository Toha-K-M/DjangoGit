from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from .GitRepo import GitRepo
from datetime import datetime
import json
from django.contrib.postgres.fields import JSONField
# Create your models here.
class Pusher(models.Model):
    name = models.CharField(max_length=250, blank=True) 
    email = models.CharField(max_length=250, blank=True) 

class Sender(models.Model):
    git_username = models.CharField(max_length=100, blank=True) 
    sender_id = models.CharField(max_length=50, blank=True)

class PullRequest(models.Model):
    number = models.IntegerField(blank=True, null=True)
    pull_id =  models.IntegerField(blank=True, null=True)
    html_url = models.CharField(max_length=250, blank=True)

class GitEvents(models.Model):
    payload = JSONField(blank=True, null=True)
    repository = models.ForeignKey(GitRepo, related_name='gitevents_repository', blank=True, 
                                        null=True, on_delete=models.SET_NULL)
    ref = models.CharField(max_length=250, blank=True)
    before = models.CharField(max_length=250, blank=True)
    after =  models.CharField(max_length=250, blank=True)
    pusher =  models.ForeignKey(Pusher, related_name='gitevents_pusher', blank=True, 
                                        null=True, on_delete=models.SET_NULL)
    sender =  models.ForeignKey(Sender, related_name='gitevents_sender', blank=True, 
                                        null=True, on_delete=models.SET_NULL)
    pull_request = models.ForeignKey(PullRequest, related_name='gitevents_pull_request', blank=True, 
                                        null=True, on_delete=models.SET_NULL)
    base_ref = models.CharField(max_length=250, blank=True, null=True)
    compare = models.CharField(max_length=250, blank=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    pushed_at = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    is_pull_request = models.BooleanField(default=False)
    is_push = models.BooleanField(default=False)
    action = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.before

