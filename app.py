from functools import wraps
from flask import Flask, flash, redirect, render_template, request, session, abort, send_from_directory, url_for
import os

app = Flask(__name__)

users = ['USER1','USER2']
drivers = ['DRIVER']

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

@app.route('/', methods=['GET'])
@login_required
def login_get():
    if 'username' in session and session['username'] in users:
        return render_template("user_main.html")
    elif 'username' in session:
        return render_template("driverIndex.html")
    else:
        login_page()


@app.route('/send_package')
def get_send_package_page():
    data = []
    return render_template('send_package.html', data = data)

@app.route('/driverIndex')
def driverIndex():
    data = []
    return render_template('driverIndex.html', data = data)


@app.route('/driverPickingUp')
def driverPickingUp():
    data = []
    return render_template('driverPickingUp.html', data = data)


@app.route('/get_package')
def get_receive_package_page():
    data = []
    return render_template('get_package.html', data = data)


@app.route('/driverRequestsList',methods=['GET'])
@login_required
def driverRequestsList():
    return render_template('driverRequestsList.html')


@app.route('/driverRequestsHistory',methods=['GET'])
@login_required
def driverRequestsHistory():
    return render_template('driverRequestsHistory.html')


@app.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    session.pop('logged_in', None)
    return login_page()


@app.errorhandler(404)
@login_required
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')


@app.route('/driverRequestInfo2',methods=['GET'])
@login_required
def driverRequestInfo2():
    return render_template('driverRequestInfo2.html')


@app.route('/driverRequestInfo',methods=['GET'])
@login_required
def driverRequestInfo():
    return render_template('driverRequestInfo.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['username'].upper() in users and request.form['password'] == '12345':
        session['user'] = request.form['username']
        session['logged_in'] = True
        return render_template("user_main.html")
    elif request.form['username'].upper() in drivers and request.form['password'] == '12345':
        session['user'] = request.form['username']
        session['logged_in'] = True
        return render_template("driverIndex.html")    
    flash('Error! The credentials are not valid, please verify!')
    return login_page()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
