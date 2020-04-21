from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class GitRepo(models.Model):
    owner = models.ForeignKey(User, related_name='gitrepo_owner', on_delete=models.CASCADE)
    id_repo = models.IntegerField()
    name = models.CharField(max_length=250)
    create_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name