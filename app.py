from flask import Flask, session, escape, render_template, redirect, request, url_for
import db
import os

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

@app.route('/to_upload')
def to_upload():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    # 'image'는 HTML 코드에서 formData.append() 메서드에서 사용한 키입니다.
    
    # 업로드된 파일의 저장 경로와 파일 이름을 지정합니다.
    file_path = '/path/to/save/directory/' + file.filename
    print(file.filename)
    print(file_path)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    # 업로드된 파일의 URL을 생성합니다.
    url = url_for('static', filename=file.filename)
    print(url)
    
    # 지정된 경로와 파일 이름으로 파일을 저장합니다.
    file.save(file_path)
    

   # 이미지 파일을 포함하는 HTML 파일을 렌더링합니다.
    return render_template('image.html', url=url)


# 로그아웃
@app.route('/out')
def end():
    session.pop('user_id', None)
    return render_template('Login.html')

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port='5500')
