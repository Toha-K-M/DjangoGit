from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from .GitRepo import GitRepo
from datetime import datetime
import json
from django.contrib.postgres.fields import JSONField

class GitEvents(models.Model):
    payload = JSONField(blank=True, null=True)

    is_pull_request = models.BooleanField(default=False)
    is_push = models.BooleanField(default=False)
    action = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.before

