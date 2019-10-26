from google.cloud import vision
import instaloader
from flask import Flask, render_template, redirect, request, flash
import logosearch

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api/instasearch/<p>', methods=['GET', 'POST'])
def apiinstaquery():
    logosearch.instasearch('its_ian_costa')
    pass #replace with code to scrape insta page, and find and display logos

if __name__ == '__main__':
    app.run()
