from flask import Flask, render_template, request
import os
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    data = [os.name, datetime.datetime.now(), request.user_agent]
    return render_template('index.html', data=data)


@app.route('/about')
def about():
    data = [os.name, datetime.datetime.now(), request.user_agent]
    return render_template('about.html', data=data)


@app.route('/portfolio')
def portfolio():
    data = [os.name, datetime.datetime.now(), request.user_agent]
    return render_template('portfolio.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
