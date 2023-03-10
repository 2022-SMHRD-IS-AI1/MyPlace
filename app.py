from flask import Flask, session, render_template, redirect, request, url_for, send_from_directory, abort, jsonify
from flask_cors import CORS
import requests
from datetime import datetime
import uuid
import db
import os



app = Flask(__name__, template_folder='templates')
CORS(app)
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

@app.route('/to_upload', methods=['GET', 'POST'])
def to_upload():
    return render_template('upload.html')


@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        # 업로드된 파일을 처리하는 로직을 작성합니다.
        file = request.files['myFileUpload']
        # 파일을 저장하고 경로를 다른 페이지로 전달합니다.
        file_path = save_file(file)
        return redirect('/result?file_path=' + file_path)
    else:
        return render_template('upload.html')

@app.route('/result')
def result():
    file_path = request.args.get('file_path')
    # 결과 페이지를 렌더링합니다.
    return render_template('result.html', file_path=file_path)

def save_file(file):
    # 파일을 저장하고 저장된 파일의 경로를 반환합니다.
    file_path = 'C:/Users/777/Documents/GitHub/MyPlace/static/images/user_img' + file.filename
    file.save(file_path)
    return file_path

# @app.route('/image', methods=['GET', 'POST'])
# def image():
#     return render_template('image.html')

# @app.route('/image/<data>', methods=['GET', 'POST'])
# def image(data):
#     return render_template('image.html', data=data)

    # if request.method == 'POST':
    #     file = request.files['image']
    # # 'image'는 HTML 코드에서 formData.append() 메서드에서 사용한 키
    
    # # 업로드된 파일의 저장 경로와 파일 이름을 지정
    #     now = datetime.now()
    #     folder_name = now.strftime('%Y-%m-%d')
    #     folder_path = os.path.join(app.root_path, 'static', folder_name)
    #     if not os.path.exists(folder_path):
    #         os.makedirs(folder_path)
    #     print(folder_path)
    #     file_name = str(uuid.uuid4()) + '.' + file.filename.split('.')[-1]
    #     file_path = os.path.join(folder_path, file_name)
    #     print(file_path)
    
    # # 지정된 경로와 파일 이름으로 파일을 저장
    #     file.save(file_path)

    # # 업로드된 파일의 URL을 생성
    #     url = url_for('static', filename=os.path.join(folder_name, file_name), _external=True)
    #     response = {
    #         'status': 'success',
    #         'url': url
    #     }
    #     return jsonify(response)
    
    
    
@app.route('/properties', methods=['GET', 'POST'])
def properties():
    return render_template('properties.html')

@app.route('/PayApi', methods=['GET', 'POST'])
def PayApi():
    return render_template('PayApi.html')

@app.route('/services', methods=['GET', 'POST'])
def services():
    return render_template('services.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/property-single')
def single():
    return render_template('property-single.html')

@app.route('/imageapi')
def api():
    return render_template('imageapi.html')

@app.route('/Easter')
def kakao():
    return render_template('Easter.html')

@app.route('/imageapi')
def imageapi():
    return render_template('imageapi.html')


# 로그아웃
@app.route('/out', methods=['GET'])
def end():
    session.pop('user_id', None)
    return render_template('Login.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5500')