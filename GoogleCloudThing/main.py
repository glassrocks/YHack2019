from google.cloud import vision
import instaloader
from flask import Flask, render_template, redirect, request, flash
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/instasearch', methods=['POST'])
def findandshow():
    pass #replace with code to scrape insta page, and find and display logos

if __name__ == '__main__':
    app.run()
