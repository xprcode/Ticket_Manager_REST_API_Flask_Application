import smtplib
import ssl
from collections import namedtuple

Credentials = namedtuple('Credentials', 'username password')

class EmailSender:
    def __init__(self, port, smtp_adress, credentials, ssl_enable=False):
        self.port = port
        self.smtp_adress = smtp_adress
        self.ssl_enable = ssl_enable
        self.connection = None
        self.credentials = credentials
    
    def __enter__(self):
        if not self.ssl_enable:
            self.connection = smtplib.SMTP(self.smtp_adress, self.port)
        else:
            context = ssl.create_default_context()
            self.connection = smtplib.SMTP_SSL(self.smtp_adress, self.port, context)
        
        self.connection.login(self.credentials.username, self.credentials.password)

        return self
    
    def sendmail(self, sender, receiver, message):
        self.connection.sendmail(sender, receiver, message)
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.connection.close()