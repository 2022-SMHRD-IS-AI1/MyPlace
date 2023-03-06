from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
app = Flask(__name__)
'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    
   
id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(
    username =
100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form[
        # username = 데이터베이스
'user']
        password = request.form[
        # password = 데이터베이스
'pass']
        user = User.query.filter_by(username=username, password=password).first()
        
        user = User.query.filter_by(username=username, password=password
if user:
     # 로그인 성공시 메인 페이지로 이동
     return redirect('index.html')
else:
    # 로그인 실패시 에러 메시지 출력
     error = 
     error =
"아이디 또는 비밀번호가 잘못되었습니다."
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['user']
        password = request.form[
        password = request.form
'pass']
        confirm_password = request.form['pass_confirm']
        email = request.form['email']
        user = User.query.filter_by(username=username).first()
        
        user
if user:
            # 이미 존재하는 아이디일 경우 에러 메시지 출력
            error = 
            error
"이미 존재하는 아이디입니다."
            
           
return render_template('register.html', error=error)
        else:
            # 새로운 사용자 추가
            new_user = User(username=username, password=password, email=email)
            db.session.add(new_user)
            db.session.commit()
            
            new_user = User(username=username, password=password, email=email)
            db.session.add(new_user)
            db.session.commit()
           

            new_user = User(username=username, password=password, email=email
# 회원가입 완료 후 로그인 페이지로 이동
            return redirect('/')
    else:
        return render_template('Loing.html')

if __name__ == '__main__':
    app.run(debug=True)