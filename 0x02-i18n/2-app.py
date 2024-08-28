#!/usr/bin/env python3
""" 2-app.py
    A simple flask ask implementing i18n and i10n
"""


from flask import Flask, render_template, request
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
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    

app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Function find the best match for the supported languages.
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    return request.accetpt_languages.best_match(app.config["LANGUAGES"])
  

@app.route('/')
def home():
    """Home page
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port="5000", host='0.0.0.0')
