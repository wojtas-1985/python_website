#!/usr/bin/python
from flask import Flask, escape, request
from flask import Flask, url_for
from markupsafe import escape
from flask import render_template
import logging

# Create an instance of this class
app = Flask(__name__)

# Logging configuration
logging.basicConfig(filename='demo.log', level=logging.DEBUG)

# Use the route() decorator to bind a function to a URL.
@app.route('/')
def index():
    app.logger.info('Processing default request')
    #return 'Index Page'
    return render_template('index.html')

@app.route('/index.html')
def index_html():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# You can add variable sections to a URL by marking sections with <variable_name>. 
@app.route('/<username>')
def hello_html(username=None):
    return render_template('username.html', name=username)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
        # data =request.form['email']
        data = request.form.to_dict()
        print(data)
        return('form submitted')
    else:
        error = 'some error'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')