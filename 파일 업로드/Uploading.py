from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    # 'image'는 HTML 코드에서 formData.append() 메서드에서 사용한 키입니다.
    
    # 업로드된 파일의 저장 경로와 파일 이름을 지정합니다.
    file_path = '/path/to/save/directory/' + file.filename

    # 업로드된 파일의 URL을 생성합니다.
    url = url_for('static', filename=file.filename)
    
    # 지정된 경로와 파일 이름으로 파일을 저장합니다.
    file.save(file_path)
    

   # 이미지 파일을 포함하는 HTML 파일을 렌더링합니다.
    return render_template('image.html', url=url)

if __name__ == '__main__':
    app.run(port=5500)