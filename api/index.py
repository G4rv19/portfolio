from flask import Flask, render_template, request, redirect, url_for
from js import inject


app = Flask(__name__)
inject()
@app.route('/')
def homepage():
    return render_template('home.html')
    
if __name__ == "__main__":
    app.run(debug=True)
