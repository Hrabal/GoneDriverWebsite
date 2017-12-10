# -*- coding: utf-8 -*-
import locale
from flask import Flask
import logging

locale.setlocale(locale.LC_TIME, locale.getlocale())

app = Flask(__name__)
app.config.from_object('config')

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

import models
import views
