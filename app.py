#! usr/bin/env python

from flask import Flask, render_template, request, g, jsonify
from sqlalchemy import create_engine
import os
# from flask_compress import Compress
# from datetime import date, timedelta


# Configuration
# SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
# Compress(app)


@app.route('/')
def index():
    return render_template('index.html')


# This works but you really should use `flask run`
if __name__ == '__main__':
    app.run()
