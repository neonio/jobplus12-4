#!/usr/bin/env bash

conda create -n myenv python=3.6

export FLASK_APP=manage.py
flask db init
flask db migrate -m "init"
flask db upgrade