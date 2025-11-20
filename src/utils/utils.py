import datetime
import hashlib
import json
import logging
import os
import re
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Tuple, Union

from cryptography.fernet import Fernet
from pydantic import BaseModel

logger = logging.getLogger(__name__)

def generate_secret_key() -> str:
    return Fernet.generate_key().decode('utf-8')

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def send_email(subject: str, body: str, sender: str, recipient: str, password: str) -> bool:
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls(context=ssl.create_default_context())
    server.login(sender, password)
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()
    return True

def validate_uuid(uuid: str) -> bool:
    pattern = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')
    return bool(pattern.match(uuid))

def validate_email(email: str) -> bool:
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return bool(pattern.match(email))

def validate_date(date_string: str) -> bool:
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
    except ValueError:
        return False
    return True

def load_config() -> dict:
    try:
        with open('config.json') as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        logger.error('Config file not found')
        return {}
    return config