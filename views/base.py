# -*- coding: utf-8 -*-
from app import app

from templates.home import Home

@app.route('/')
def index():
    return Home().render()
