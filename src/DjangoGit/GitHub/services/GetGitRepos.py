import logging
import requests, json

from service_objects.services import Service
from rest_framework.exceptions import PermissionDenied
from ... import application_properties
from ..models import GitRepo
# from django.contrib.auth.models import User

logger = logging.getLogger("error_logger")

class GetPublicRepos(Service):
    def service_clean(self):
        current_user = self.files.get("current_user")
        if current_user is None or current_user.is_authenticated is False:
            raise PermissionDenied()

    def process(self):
        try:
            def isSelected(repos):
                for item in repos:
                    if GitRepo.objects.filter(id_repo=item['id']).exists():
                        item['isSelected'] = True
                    else: item['isSelected'] = False


            current_user = self.files.get("current_user")
            if current_user.gitprofile.access_token:
                api = 'https://api.github.com/users/'+current_user.gitprofile.git_username+'/repos'
                access_token = current_user.gitprofile.access_token
                response = requests.get(api, headers={'Authorization': 'token '+access_token})

                if response.status_code == 200:
                    repos = response.json()
                    isSelected(repos)
                    return repos, None
                return None, response.status_code
            else:
                return None, 401

        except Exception as e:
            logger.error(repr(e))
            return None