from concurrent.futures.process import _python_exit
import sys
import os
import secrets
import hashlib
from unicodedata import name
import mysql.connector
import re
from time import sleep
from datetime import datetime




class Bank:
    def __init__(self, name, phone, pin):
            self.name = name
            self.phone = phone
            self.pin = hashlib.sha256(pin.encode()).hexdigest()
            self.account_number = self.create_account_number()
            self.balance = 0
            self.account_number_login = ''
            self.create_database()

    def connect_db(self):
        try:
            conn = mysql.connector.connect(
                host='localhost'

            )

