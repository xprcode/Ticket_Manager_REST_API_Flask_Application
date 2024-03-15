from datetime import datetime
import email
from os import getenv
import sqlite3


from dotenv import load_dotenv



load_dotenv()

connection = sqlite3.connect('baza.db')

ssl_enable = getenv('SSL_ENABLE')
port = getenv('PORT')
smtp_server = getenv('SMTP_SERVER')
username = getenv('MAIL_USERNAME')
password = getenv('MAIL_PASSWORD')

sender = getenv('SENDER')
