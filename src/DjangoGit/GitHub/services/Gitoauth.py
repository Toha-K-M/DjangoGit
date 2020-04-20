import logging
import requests, json

from service_objects.services import Service
from rest_framework.exceptions import PermissionDenied
from ... import application_properties
# from django.contrib.auth.models import User

logger = logging.getLogger("error_logger")

class access_token_is_valid(Service):
    def service_clean(self):
        current_user = self.files.get("current_user")
        if current_user is None or current_user.is_authenticated is False:
            raise PermissionDenied()

    def process(self):
        try:
            current_user = self.files.get("current_user")
            if current_user.gitprofile.access_token:
                api = 'https://api.github.com/user'
                access_token = current_user.gitprofile.access_token
                response = requests.get(api, headers={'Authorization': 'token '+access_token})
                if response.status_code == 401:
                    print('Bad Credentials')
                    return False
                return True
            else:
                return False

        except Exception as e:
            logger.error(repr(e))
            return None

class get_access_token(Service):
    def service_clean(self):
        current_user = self.files.get("current_user")
        if current_user is None or current_user.is_authenticated is False:
            raise PermissionDenied()

    def process(self):
        try:
            current_user = self.files.get("current_user")

            def save_current_user_oauth(response):
                current_user.gitprofile.access_token = response['access_token']
                current_user.gitprofile.token_type = response['token_type']  
                current_user.gitprofile.scope = response['scope']      
                current_user.save()

            url = "https://github.com/login/oauth/access_token"
            code = self.data.GET['code']
            payload = {
                "code":code,
                "client_secret":application_properties.client_secret,
                "client_id":application_properties.client_id
            }
            headers = {'Accept': 'application/json'}
            response = requests.post(url, payload, headers=headers).json()
            
            save_current_user_oauth(response)

            return True

        except Exception as e:
            logger.error(repr(e))
            return None