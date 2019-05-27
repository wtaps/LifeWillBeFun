from flask import Flask, url_for, request, render_template, flash, make_response, redirect, escape, session
app = Flask(__name__)
app.secret_key = ''

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/index')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return render_template('login.html')
    #return redirect(url_for('login'))

@app.route('/user/<username>')
def show(username):
    return 'Life Will Be Fun %s' % username

@app.route('/show/<int:post_id>')
def post(post_id):
    return 'Life Will Be Fun %d' % post_id

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    #if request.method == 'POST':
    #    if len(request.form['username']) < 8 or len(request.form['password']) < 8:
    #        error = 'username or password is invalid'    
    #    else:
    #        error = 'login success, please access other page'
    #else:
    #    return 'error not support get method'
    #return render_template('login_result.html', error=error)
    #
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/send_cookie', methods=['GET', 'POST'])
def send_cookie():
    resp = make_response(render_template('login.html'))
    resp.set_cookie('username', 'tony')
    return resp

@app.route('/recv_cookie', methods=['GET', 'POST'])
def recv_cookie():
    username = request.cookies.get('username')
    return username

@app.route('/bbc')
def bbc():
    return redirect(url_for('send_cookie'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
