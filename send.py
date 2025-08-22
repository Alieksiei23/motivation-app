import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

sender = 'motivappt@mail.ru'
password = os.getenv('EMAIL_PASSWORD')

getter = 'rawifi6008@namestal.com'

server = smtplib.SMTP('smtp.mail.ru', 587)
server.starttls()

server.login(sender, password)
server.sendmail(sender, getter, 'fafasf')