from functools import wraps
from flask import Flask, flash, redirect, render_template, request, session, abort, send_from_directory, url_for
import os

app = Flask(__name__)

app.secret_key = os.urandom(12)

app.config.update(
    DEBUG = True,
)

def login_required(f):
    @wraps(f)
    def login_ann(*args, **kwargs):
        if 'logged_in' in session and not session['logged_in']:
            return login_page()
        elif 'logged_in' not in session:
            return login_page()
        return f(*args, **kwargs)
    return login_ann

def login_page():
    return render_template('login.html')

@app.route('/login', methods=['GET'])
@login_required
def login_get():
    return redirect(url_for('index'))

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
@app.route('/index',methods=['GET'])
@login_required
def index():
    return render_template('index.html')

@app.route('/user',methods=['GET'])
@login_required
def user():
    return render_template('user.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('user', None)
    session.pop('logged_in', None)
    return login_page()

@app.errorhandler(404)
@login_required
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        session['user'] = request.form['username']
        session['logged_in'] = True
    else:
        flash('Error! The credentials are not valid, please verify!')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='localhost', port=4000)
