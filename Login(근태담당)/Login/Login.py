from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # 여기에서 username과 password를 검증하는 코드를 작성합니다.
    # ...

    return '로그인 성공'

if __name__ == '__main__':
    app.run(debug=True)
