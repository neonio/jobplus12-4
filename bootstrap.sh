#!/usr/bin/env bash
conda create -n myenv

export FLASK_APP=manage.py
flask db init
flask db migrate -m "init"
flask db upgrade