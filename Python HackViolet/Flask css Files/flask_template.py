from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/search/')
def search():
    return '<h3> Words Entered into search bar: </h3>'

@app.route('/contact/')
def about():
    return render_template('contact.html')

app.run(0.0)

