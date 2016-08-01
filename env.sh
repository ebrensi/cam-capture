#! usr/bin/env bash

source activate flask

export DATABASE_URL=postgresql://efrem:efrem@localhost/efrem
export FLASK_APP=app.py
export FLASK_DEBUG=1

