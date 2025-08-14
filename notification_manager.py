from twilio.rest import Client
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.account_sid = os.getenv("account_sid")
        self.auth_token = os.getenv("auth_token")
        self.smtp_address = os.getenv("smtp_email")
        self.smtp_password = os.getenv("smtp_password")
        self.api_key = os.getenv("api_key")
        self.twilio_from = os.getenv("twilio_from")
        self.twilio_to = os.getenv("twilio_to")

    def notify(self, price, your_city, destination, takeoff, return_date, emails):
        body = (
            f"Low Price Alert! Only £{price} to fly from {your_city} to {destination}, "
            f"on {takeoff} until {return_date}"
        )
        try:
            self.send_sms(body)
            self.send_mail(emails, body)
            print("✔️ Notification sent.")
        except Exception as e:
            print(f"⚠️ Notification error: {e}")

    def indirect_flight(self, body, emails):
        try:
            self.send_sms(body)
            self.send_mail(emails, body)
            print("✈️ Indirect flight info sent.")
        except Exception as e:
            print(f"⚠️ Indirect flight notification error: {e}")

    def send_sms(self, body):
        client = Client(self.account_sid, self.auth_token)
        client.messages.create(
            from_=self.twilio_from,
            body=body,
            to=self.twilio_to
        )

    def send_mail(self, emails, message):
        for i in emails:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(self.smtp_address, self.smtp_password)
                email_msg = f"Subject: Flight Alert!\n\n{message}"
                connection.sendmail(
                    from_addr=self.smtp_address,
                    to_addrs=i,
                    msg=email_msg.encode("utf-8")
                )
