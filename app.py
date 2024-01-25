from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def default_redirect():
    return redirect(url_for('homepage'))

@app.route('/home')
def homepage():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
