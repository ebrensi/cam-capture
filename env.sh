#! usr/bin/env bash

source activate flask

export DATABASE_URL=postgresql://camcapp:camcapp@localhost/camcapp
export FLASK_APP=app.py
export FLASK_DEBUG=1

