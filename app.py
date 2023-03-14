from flask import Flask, session, render_template, redirect, request, url_for, send_from_directory, abort, jsonify
from flask_cors import CORS
import requests
from datetime import datetime
import uuid
import db
import os
import time



app = Flask(__name__, template_folder='templates')
CORS(app)
app.config['UPLOAD_FOLDER'] = 'C:/Users/777/Documents/GitHub/MyPlace/static' # 업로드 파일 경로 설정
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.secret_key = 'my_secret_key'

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# def save_file(file):
#     # 파일을 저장하고 저장된 파일의 경로를 반환합니다.
#     file_name = file.filename
#     file_ext = os.path.splitext(file_name)[1]
#     unique_name = str(int(time.time())) + file_ext
#     file_path = os.path.join(os.getcwd(), 'uploads', unique_name)
#     print('save_file_path :', file_path)
#     file.save(file_path)
#     return file_path

@app.route('/')
def go():
    return render_template('Introduction.html')

@app.route('/Login')
def IntrLogin():
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
            return redirect(url_for('IntrLogin'))
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
    #id = session['user_id']
    return render_template('index.html', error=error)#, id=id

@app.route('/to_upload', methods=['GET', 'POST'])
def to_upload():
    return render_template('upload.html')


# @app.route('/upload', methods=['GET','POST'])
# def upload():
#     if request.method == 'POST':
#         file = request.files['myFileUpload']
#         # 업로드된 파일의 저장 경로와 파일 이름을 지정
#         now = datetime.now()
#         folder_name = now.strftime('%Y-%m-%d')
#         folder_path = os.path.join(app.root_path, 'static', folder_name)
#         if not os.path.exists(folder_path):
#             os.makedirs(folder_path)
#         print(folder_path)
#         file_name = str(uuid.uuid4()) + '.' + file.filename.split('.')[-1]
#         file_path = os.path.join(folder_path, file_name)
#         print('file_path', file_path)

#         # 지정된 경로와 파일 이름으로 파일을 저장
#         file.save(file_path)

#         file_path.replace('\\','/')
#         print(file_path.find('static'))
#         file_path=file_path[38:]
        
#         return redirect(url_for('analyze', file_path=file_path))
#     else:
#         return render_template('upload.html')


# @app.route('/image')
# def image():
#     file_path = request.args.get('file_path')
#     print('제발', file_path)
#     # 결과 페이지를 렌더링합니다.
#     return render_template('image.html', file_path=file_path)

@app.route('/analyze', methods=['GET','POST'])
def analyze():
    file_path = request.args.get('file_path')
    url = "https://apis.openapi.sk.com/urbanbase/v1/space/analyzer"
    # payload = "{\"image_path\":\"https://www.ikea.com/images/2-e4e271bd007a75af466351b6828af61c.jpg\"}"
    payload = "{\"image_path\":\""+file_path+"\"}"
    print('Payload :',payload)
    headers = {
        "accept": "application/json",
        "Content-Type": "json",
        "appKey": "XMGz6G5jzF5nybARW4cmY7fck4vpDiqg5u44kvRH"
    }

    response = requests.post(url, data=payload, headers=headers)

    print('txt : ',response.text)
    # print(response.text.find('[{"label"'))
    # print(response.text.find('],"created_date'))
    start = response.text.find('[{"label"')
    end = response.text.find('],"created_date')
    result=response.text[start:end+1]
    # print(result.find('[{"label"'))
    # print(result.find('},{'))
    cut=result.find('},{')
    result=result[:cut+1]
    print('result : ',result)
    
    ### result
    label_start = result.find('":"')
    label_end = result.find('","')
    label = result[label_start+3:label_end]
    find_probability = result[label_end+2:]
    probability_start = find_probability.find(':')+1
    probability_end = find_probability.find(':')+8
    probability = find_probability[probability_start:probability_end]
    description_start = find_probability.find('on":"')+5
    description = find_probability[description_start:]
    description = description.replace('"}','')
    # print(label, probability, description)
    
    
    ### dictionary
    data = {
        'label' : label,
        'probability' : probability,
        'description' : description
    }
    print(data)
    
    # return render_template('imageapi.html', data=data, file_path=file_path)
    return redirect(url_for('yolo'), data=data, file_path=file_path)

# @app.route('/yolo', method=['GET','POST'])
# def yolo():
#     file_path = request.args.get('file_path')
#     data = request.args.get('data')
    
    
#     img = img
    
#     return render_template('imageapi.html', data=data, img = img)
    
# 1. app.py 에서 함수 만들고
# 2. best_ckpt.pt(저희꺼 모델) 불러오기
# 3. 모델 실행
# 4. infer.py 안에 있는 save dir 복붙
# 5. render template
# (imageapi.html, 값 다시 보내주기 
# data = data(api돌린거), result(yolo돌린 결과값))

    
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

@app.route('/가구배치')
def aaaa():
    return render_template('가구배치.html')

@app.route('/Introduction')
def Introduction():
    return render_template('Introduction.html')

@app.route('/move_furniture')
def move_furniture():
    return render_template('move_furniture.html')



# 로그아웃
@app.route('/out', methods=['GET'])
def end():
    session.pop('user_id', None)
    return render_template('Login.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5500')