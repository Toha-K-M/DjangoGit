import logging
import requests, json
import datetime

from service_objects.services import Service
from rest_framework.exceptions import PermissionDenied
from ... import application_properties
from ..models import GitRepo, GitEvents
# from django.contrib.auth.models import User

logger = logging.getLogger("error_logger")

class SaveEvents(Service):
    def service_clean(self):
        pass
    
    def process(self):
        try:
            data = self.files.get("data")
            gitEvents = GitEvents()
            gitEvents.payload = data
            
            # if GitRepo.objects.filter(id_repo=data["repository"]["id"])

            if "pusher" in data:
                gitEvents.is_push = True
            elif "pull_request" in data:
                gitEvents.is_pull_request = True
            if "action" in data:
                gitEvents.action = data['action']
            gitEvents.created_at = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z')
            gitEvents.save()

        except Exception as e:
            logger.error(repr(e))

