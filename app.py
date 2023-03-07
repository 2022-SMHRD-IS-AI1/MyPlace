from flask import Flask, session, escape, render_template, redirect, request, url_for
import db

app = Flask(__name__, template_folder='templates')
app.secret_key = 'my_secret_key'

@app.route('/')
def go():
    return render_template('Login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error=None
    if request.method == 'POST':
        id = request.form['login_id']
        pw = request.form['login_pw']
        print(id, pw)
        
        result = db.login_check(id,pw)
        for row in result:
            data = row[0]
        if data:
            session['user_id'] = id
            return redirect(url_for('index'))
        else:
            return redirect(url_for('go'))
    return render_template('index.html', error = error)

@app.route('/regist', methods=['GET', 'POST'])
def regist():
    error = None
    if request.method == 'POST':
        id = request.form['join_id']
        pw = request.form['join_pw']
        email = request.form['join_mail']

        result = db.join(id,pw,email)
        if result:
            return redirect(url_for('go'))
        else:
            return redirect(url_for('go'))
    return render_template('Login.html', error=error)

@app.route('/index', methods=['GET', 'POST'])
def index():
    error = None
    id = session['user_id']
    return render_template('index.html', error=error, id=id)



# 로그아웃
# @app.route('/out')
# def end():
#     session.pop('username', None)
#     return 'end'

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port='5500')
