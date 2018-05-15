"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

from flaskext.markdown import Markdown
Markdown(app)


import uc_prod.views
