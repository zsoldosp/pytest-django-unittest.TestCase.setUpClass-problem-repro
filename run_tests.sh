#!/bin/bash
source ./venv/bin/activate
python manage.py test app # passes
py.test --ds=settings app/tests.py # fails
