from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

@app.route('/')
def home():
    """Home page
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port="5000",host='0.0.0.0')
