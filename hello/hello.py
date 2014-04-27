from flask import Flask, url_for, request, render_template, flash
app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/index')
def index():
    return render_template('login.html')

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
        if len(request.form['username']) < 8 or len(request.form['password']) < 8:
            error = 'username or password is invalid'    
        else:
            error = 'login success, please access other page'
    else:
        return 'error not support get method'
    return render_template('login_result.html', error=error)

#def valid_login(username, password):
#    if len(username) < 8 or len(password) < 8:
#        flash('wrong')
#    else:
#        return True
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
