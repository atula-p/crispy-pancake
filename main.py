from flask import Flask, render_template
app = Flask(__name__)

#@app.route('/')
#def hello():
#    return 'yoohoo!'


@app.route('/')
def cal():
    return render_template('index.html')


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


if __name__ == '__main__':
    app.run(debug=True)