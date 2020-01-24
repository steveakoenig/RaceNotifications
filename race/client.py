from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import os

class SMSClient:

    def __init__(self):
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.twilio_number = os.getenv('TWILIO_PHONE_NUMBER')
        print(account_sid)
        print(auth_token)
        print(self.twilio_number)

        self.client = Client(account_sid, auth_token)


    def send_sms(self, text, destinations):
        for number in destinations:
            try:
                message = self.client.messages \
                        .create(body = text, from_ = self.twilio_number, to = number)

                if message.status in ['undelivered','failed']:
                    print('Failed to send message to {0}, failed with error {1}'\
                            .format(number, message.error_message))
                
            except TwilioRestException as err:
                print('Failed to send message to {0}, failed with error {1}'\
                        .format(number, err))

