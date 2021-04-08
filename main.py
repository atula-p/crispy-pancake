from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)


@babel.localeselector
def get_locale():
    return 'de'
    #request.accept_languages.best_match(['en', 'de'])

#@app.route('/')
#def hello():
#    return 'yoohoo!'


@app.route('/')
def index():
    driving_school = gettext('Driving School')
    greetings = gettext('Hi, how are you?')
    answer = gettext('I am fine')
    return render_template('index.html', driving_school=driving_school, greetings=greetings, answer=answer)


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