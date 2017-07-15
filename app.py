from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def home():
    #page = request.args.get('page')
    data = []
    return render_template('index.html', data = data)
@app.route('/user')
def get_main_user_page():
    #page = request.args.get('page')
    data = []
    return render_template('user_main.html', data = data)
@app.route('/send_package')
def get_send_package_page():
    #page = request.args.get('page')
    data = []
    return render_template('send_package.html', data = data)
@app.route('/get_package')
def get_receive_package_page():
    #page = request.args.get('page')
    data = []
    return render_template('get_package.html', data = data)
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='localhost', port=4000)
