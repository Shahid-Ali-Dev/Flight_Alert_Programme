
from dotenv import load_dotenv
import os
import requests
load_dotenv()
class DataManager:
    def __init__(self):
        self.header = {
            "Authorization": os.getenv("Authorization_offers")}
        self.sheet_url = f"{os.getenv("base_sheety_url")}/prices"
        self.users = requests.get(f"{os.getenv("base_sheety_url")}/users",headers=self.header)
        self.response = requests.get(url=self.sheet_url,headers=self.header)
        self.sheet_data = self.response.json()['prices']
        self.emails = self.get_emails()

    def put(self,para,i):
        sheet_update = requests.put(url=f"{self.sheet_url}/{i}",headers=self.header,json=para)

    def get_emails(self):
        return [user["writeYourEmail"] for user in self.users.json()["users"]]


