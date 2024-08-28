#!/usr/bin/env python3
""" 1-main.py
    A simple flask app representig internationalization and localization 
"""


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """Class to set the configuration for the app.
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LANGUAGE = 'en'
    BABEL_DEFAULT_TIMEZONE ='UTC'

app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """Home page
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    return render_template('1-index.html')
    

if __name__ == '__main__':
    app.run(debug=True, port="5000", host='0.0.0.0')
