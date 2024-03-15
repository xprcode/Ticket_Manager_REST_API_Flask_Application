from datetime import datetime
import email
from os import getenv
from string import Template
from dotenv import load_dotenv

from user_and_event import get_user_and_event
from emails import Credentials, EmailSender

load_dotenv()

ssl_enable = getenv('SSL_ENABLE')
port = getenv('PORT')
smtp_server = getenv('SMTP_SERVER')
username = getenv('MAIL_USERNAME')
password = getenv('MAIL_PASSWORD')

sender = getenv('SENDER')

credentials = Credentials(username, password)

def send_remainder_to_borrowers():
    
        template = Template('''
        ''')
        text = template.substitute({
            'name': borower.name,
            'title': borower.title,
            'return_at': borower.return_at
        })

        message = email.message_from_string(text)
        message.set_charset('utf-8')
        message['From'] = sender
        message['To'] = borower.email
        message['Subject'] = ''
        connection.sendmail(sender, borower.email, message.as_string())


def send_by_EmailSender(user_id, event_id):
    
    event_confirmation  =  get_user_and_event(connection, datetime.today().strftime('%Y-%m-%d'))

    with EmailSender(port, smtp_server, credentials) as connection:
        send_remainder_to_borrowers(event_confirmation, connection)