from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def home():
    #page = request.args.get('page')
    data = []
    return render_template('index.html', data = data)

@app.route('/driver')
def driver():
        return render_template('driver.html')

@app.route('/user')
def user():
    #page = request.args.get('page')
    data = []
    return render_template('user_main.html', data = data)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='localhost', port=4000)

