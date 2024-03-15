"""
Email Sending Utility

This module provides a utility for sending emails using the SMTP protocol.
It defines a class `EmailSender` that encapsulates the functionality for 
establishing a connection to an SMTP server and sending emails.

Attributes:
    - Credentials: Namedtuple to store email credentials (username, password).
"""

from collections import namedtuple
import smtplib
import ssl


Credentials = namedtuple('Credentials', 'username password')

class EmailSender:
    """
        Initializes EmailSender instance.

        Args:
            port (int): Port number for SMTP server.
            smtp_address (str): SMTP server address.
            credentials (namedtuple): Email credentials (username, password).
            ssl_enable (bool, optional): Whether to enable SSL encryption. Defaults to False.
        """
    def __init__(self, port, smtp_adress, credentials, ssl_enable=False):
        self.port = port
        self.smtp_adress = smtp_adress
        self.ssl_enable = ssl_enable
        self.connection = None
        self.credentials = credentials

    def __enter__(self):
        """
        Establishes connection to SMTP server.

        Returns:
            EmailSender: Instance of EmailSender.
        """
        if not self.ssl_enable:
            self.connection = smtplib.SMTP(self.smtp_adress, self.port)
        else:
            context = ssl.create_default_context()
            self.connection = smtplib.SMTP_SSL(self.smtp_adress, self.port, context)

        self.connection.login(self.credentials.username, self.credentials.password)

        return self

    def sendmail(self, sender, receiver, message):
        """
        Sends email message.
        """
        self.connection.sendmail(sender, receiver, message)

    def __exit__(self, exc_type, exc_value, exc_tb):
        """
        Closes the SMTP connection.
        """
        self.connection.close()
