import os
import requests
from dotenv import load_dotenv
load_dotenv()
class FlightSearch:
    def __init__(self):
        self.amend_api_key = os.getenv("amend_api_key")
        self.amend_secret = os.getenv("amend_secret")
        self.token = self.get_new_token()

    def get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            "grant_type": "client_credentials",
            "client_id": self.amend_api_key,
            "client_secret": self.amend_secret
        }
        response = requests.post("https://test.api.amadeus.com/v1/security/oauth2/token", data=body,
                                 headers=header).json()
        return response['access_token']

