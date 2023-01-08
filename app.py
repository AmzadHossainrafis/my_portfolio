#import flask 
from flask import Flask, render_template, request, redirect, url_for, flash 







# Create an instance of Flask 
app = Flask(__name__) 
#home page 
@app.route('/') 
def home(): 
    return render_template('home.html') 

if __name__ == '__main__': 
    app.run(debug=True) 
    