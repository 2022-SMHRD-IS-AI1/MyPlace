from flask import Flask, session, escape, render_template, redirect, request, url_for
import cx_Oracle

app = Flask(__name__, template_folder='templates')
app.secret_key = "ABCDEFG"

@app.route('/')
def go():
    error=None
    return render_template('Login.html', error = error)

app.secret_key = "ABCDEFG"
@app.route('/Login.html', methods=['GET', 'POST'])
def login():
    if not cx_Oracle.init_oracle_client:
        cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_9")

    #연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
    conn = cx_Oracle.connect('kgt1234','123456a','project-db-stu.ddns.net:1524/xe', encoding="UTF-8")

    cursor = conn.cursor()

    app.config['db_connection'] = conn
    
    error=None
    if request.method == 'POST':
        id = request.form['login_id']
        pw = request.form['login_pw']

        conn = cx_Oracle.connect()
        cursor = conn.cursor()
        sql = "SELECT * FROM my_user WHERE user_id = %s AND user_pw = %s"% (id, pw)
        value = (id, pw)
        cursor.execute("set names utf8")
        cursor.execute(sql, value)

        data = cursor.fetchall()
        cursor.close()
        conn.close()
        
        for row in data:
            data = row[0]

        if data:
            session['user'] = id
            return redirect(url_for('index'))
        else:
            error = 'invalid input data detected !'
    return render_template('index.html', error = error)

@app.route('/Login.html', methods=['GET', 'POST'])
def regist():
    if not cx_Oracle.init_oracle_client:
        cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_9")

    #연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
    conn = cx_Oracle.connect('kgt1234','123456a','project-db-stu.ddns.net:1524/xe', encoding="UTF-8")

    cursor = conn.cursor()

    app.config['db_connection'] = conn
    
    error = None
    if request.method == 'POST':
        id = request.form['join_id']
        pw = request.form['join_pw']
        
 
        conn = cx_Oracle.connect()
        cursor = conn.cursor()
 
        sql = "INSERT INTO users VALUES ('%s', '%s')" % (id, pw)
        cursor.execute(sql)
 
        data = cursor.fetchall()
 
        if not data:
            conn.commit()
            return redirect(url_for('login'))
        else:
            conn.rollback()
            return "Regist Failed"
    cursor.close()
    conn.close()
 
    return render_template('Login.html', error=error)
 
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    error = None
    id = session['user']
    return render_template('index.html', error=error, id=id)



# 로그아웃
# @app.route('/out')
# def end():
#     session.pop('username', None)
#     return 'end'


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port='5500')
