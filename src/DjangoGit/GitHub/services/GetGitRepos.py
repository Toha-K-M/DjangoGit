import logging
import requests, json

from service_objects.services import Service
from rest_framework.exceptions import PermissionDenied
from ... import application_properties
# from django.contrib.auth.models import User

logger = logging.getLogger("error_logger")

class GetPublicRepos(Service):
    def service_clean(self):
        current_user = self.files.get("current_user")
        if current_user is None or current_user.is_authenticated is False:
            raise PermissionDenied()

    def process(self):
        try:
            current_user = self.files.get("current_user")
            if current_user.gitprofile.access_token:
                api = 'https://api.github.com/users/'+current_user.gitprofile.git_username+'/repos'
                access_token = current_user.gitprofile.access_token
                response = requests.get(api, headers={'Authorization': 'token '+access_token})

                if response.status_code == 200:
                    return response.json(), None
                return None, response.status_code
            else:
                print('2')
                return None, 401

        except Exception as e:
            logger.error(repr(e))
            return None