import logging
import requests, json

from service_objects.services import Service
from rest_framework.exceptions import PermissionDenied
from ... import application_properties

logger = logging.getLogger("error_logger")

class CreateHook(Service):
    def service_clean(self):
        current_user = self.files.get("current_user")
        if current_user is None or current_user.is_authenticated is False:
            raise PermissionDenied()

    def process(self):
        try:
            current_user = self.files.get("current_user")
            repo_name = self.files.get("selected_repo_name")
            git_username = current_user.gitprofile.git_username

            api = application_properties.base_api+'/repos/'+git_username+'/'+repo_name+'/hooks'
            access_token = current_user.gitprofile.access_token
            payload = {
                        "name": "web",
                        "active": True,
                        "events": [
                            "push",
                            "pull_request",
                        ],
                        "config": {
                            "url": application_properties.base_api+"/webhook/",
                            "content_type": "json",
                            "insecure_ssl": "0"
                        }
                    }
            response = requests.post(api, json.dumps(payload), headers={'Authorization': 'token '+access_token})
            if response.status_code == 201:
                return True
            return False
        except Exception as e:
            logger.error(repr(e))
            return None
