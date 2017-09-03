#!/usr/bin/env python
## -*- coding: utf-8 -*-
import os

from flask import Flask
application = Flask(__name__)

import cherrypy
from mako.template import Template
from mako.lookup import TemplateLookup

@application.route("/")
def hello():
    return "Hello Mako!"

if __name__ == "__main__":
    application.run()
