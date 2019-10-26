from google.cloud import vision
import instaloader
from flask import Flask, render_template, redirect, request, flash
from jinja2 import Template
import logosearch

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api/instasearch/<url>', methods=['GET', 'POST'])
def apiinstaquery(url):
    logo_return = logosearch.instasearch(url)
    #filter out all None values 
    logo_return = [f for f in logo_return if f]
    print(f'1: {logo_return}')
    for logo in logo_return:
        if logo is None:
            logo_return.remove(logo)
    print(f'2: {logo_return}')
    return render_template('displayimages.html')

if __name__ == '__main__':
    app.run()
