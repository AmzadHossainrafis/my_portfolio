#import flask 
from flask import Flask, render_template, request, redirect, url_for, flash 
import os 
import sqlite3






# Create an instance of Flask 
app = Flask(__name__) 
#home page 
@app.route('/') 
def home(): 
    return render_template('home.html') 

# login page 
@app.route('/loin') 
def login(): 

    return render_template('login.html')  # render a template

if __name__ == '__main__': 
    app.run(debug=True) 
    