import logging
import requests, json

from service_objects.services import Service
from rest_framework.exceptions import PermissionDenied
from ... import application_properties

logger = logging.getLogger("error_logger")

class get_access_token(Service):
    def service_clean(self):
        current_user = self.files.get("current_user")
        if current_user is None or current_user.is_authenticated is False:
            raise PermissionDenied()

    def process(self):
        try:
            url = "https://github.com/login/oauth/access_token"
            code = self.data.GET['code']
            payload = {
                "code":code,
                "client_secret":application_properties.client_secret,
                "client_id":application_properties.client_id
            }
            headers = {'Accept': 'application/json'}
            response = requests.post(url, payload, headers=headers).json()
            access_token = response['access_token']
            get_response = requests.get('https://api.github.com/user', 
                headers={'Authorization': 'token '+access_token})
            # print(get_response.json())
            return True

        except Exception as e:
            logger.error(repr(e))
            return None