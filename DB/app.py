from flask import Flask, session, render_template, redirect, request, url_for
import cx_Oracle

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '0000'
app.config['MYSQL_DATABASE_DB'] = 'user_info'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.secret_key = "ABCDEFG"
cx_Oracle.init_app(app)

#연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
conn = cx_Oracle.connect('kgt1234','123456a','project-db-stu.ddns.net:1524/xe', encoding="UTF-8")

cursor = conn.cursor()

app.config['db_connection'] = conn

@app.route('/', methods=['GET', 'POST'])
def login():

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
            session['login_user'] = id
            return redirect(url_for('index'))
        else:
            error = 'invalid input data detected !'
    return render_template('index.html', error = error)

def regist():
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
    id = session['login_user']
    return render_template('home.html', error=error, id=id)


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port='5000')