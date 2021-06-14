from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)


@babel.localeselector
def get_locale():
    return 'en'
    #request.accept_languages.best_match(['en', 'de'])

#@app.route('/')
#def hello():
#    return 'yoohoo!'


@app.route('/')
def index():
    return render_template('index_eng.html')


@app.route('/index_eng')
def index_eng():
    return render_template('index_eng.html')


@app.route('/index_ger')
def index_ger():
    return render_template('index_ger.html')


@app.route('/index_tur')
def index_tur():
    return render_template('index_tur.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/booking')
def booking():
    return render_template('booking.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/layout')
def layout():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(debug=True)