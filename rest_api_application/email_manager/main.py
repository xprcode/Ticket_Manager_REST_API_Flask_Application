"""
Email Manager

This module provides functionality for sending emails to users 
regarding event reminders and confirmations. It utilizes a template-based 
approach to compose email messages and integrates with the EmailSender 
class for sending emails.

"""
from string import Template
from os import getenv
import email
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

def send_event_confirmation(user_event, connection):
    """
    Send an event confiramtion.

    Args:
        user_event (UserEvent): User and event information.
        connection (EmailSender): EmailSender instance for sending emails.
    """

    template = Template('''Dear $name.
    Thank you for adding $event_name to your events.
    The $event_name will take place at $event_adress on $event_date.
    Once again thank you and see you at $event_adress .
    Best regards,
    Ticket_Manager_Team!
        ''')
    text = template.substitute({
            'name': user_event.name,
            'email': user_event.email,
            'event_name': user_event.event_name,
            'event_adress': user_event.event_adress,
            'event_date': user_event.event_data
        })

    message = email.message_from_string(text)
    message.set_charset('utf-8')
    message['From'] = sender
    message['To'] = user_event.email
    message['Subject'] = f'New event - {user_event.event_name}'
    connection.sendmail(sender, user_event.email, message.as_string())


def send_by_emailsender(user_id, event_id):
    """
    Send an email using EmailSender.

    Args:
        user_id (int): The ID of the user.
        event_id (int): The ID of the event.
    """
    event_confirmation  =  get_user_and_event(user_id, event_id)

    with EmailSender(port, smtp_server, credentials) as connection:
        send_event_confirmation(event_confirmation, connection)
