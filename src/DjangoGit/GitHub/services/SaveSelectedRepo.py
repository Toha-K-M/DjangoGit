import logging
import requests, json

from service_objects.services import Service
from rest_framework.exceptions import PermissionDenied
from ... import application_properties
from ..models import GitRepo
# from django.contrib.auth.models import User

logger = logging.getLogger("error_logger")

class SaveRepo(Service):
    def service_clean(self):
        current_user = self.files.get("current_user")
        if current_user is None or current_user.is_authenticated is False:
            raise PermissionDenied()

    def process(self):
        try:
            current_user = self.files.get("current_user")
            selected_repo_id = self.files.get("selected_repo_id")
            selected_repo_name = self.files.get("selected_repo_name")
            gitRepo = GitRepo()
            gitRepo.owner_id = current_user.id
            gitRepo.id_repo = int(selected_repo_id)
            gitRepo.name = selected_repo_name
            gitRepo.save()
            
            return True

        except Exception as e:
            logger.error(repr(e))
            return False