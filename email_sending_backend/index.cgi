#!/usr/bin/python
import os

### Activate the virtualenv in the current directory
activate_this = os.path.abspath(os.path.dirname(__file__)) + '/bin/activate_this.py'
assert os.path.exists(activate_this)

execfile(activate_this, dict(__file__=activate_this))

### Run our app
from wsgiref.handlers import CGIHandler
import app
CGIHandler().run(app.app)
