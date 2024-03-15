from datetime import datetime
import email
from os import getenv
from string import Template
from dotenv import load_dotenv

from rest_api_application.email_manager.user_and_event import get_user_and_event
from rest_api_application.email_manager.emails import Credentials, EmailSender

load_dotenv()

ssl_enable = getenv('SSL_ENABLE')
port = getenv('PORT')
smtp_server = getenv('SMTP_SERVER')
username = getenv('MAIL_USERNAME')
password = getenv('MAIL_PASSWORD')

sender = getenv('SENDER')

credentials = Credentials(username, password)

def send_remainder_to_borrowers(user_event, connection):
    
        template = Template('''Test
        ''')
        text = template.substitute({
            'name': user_event.name,
            'email': user_event.email,
            'event_name': user_event.event_name,
            'event adress': user_event.event_adress,
            'event_data': user_event.event_data
        })

        message = email.message_from_string(text)
        message.set_charset('utf-8')
        message['From'] = sender
        message['To'] = user_event.email
        message['Subject'] = 'Test'
        connection.sendmail(sender, user_event.email, message.as_string())


def send_by_EmailSender(user_id, event_id):
    
    event_confirmation  =  get_user_and_event(user_id, event_id)

    with EmailSender(port, smtp_server, credentials) as connection:
        send_remainder_to_borrowers(event_confirmation, connection)