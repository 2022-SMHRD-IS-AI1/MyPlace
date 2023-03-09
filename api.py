import requests
from flask import Flask, session, render_template, redirect, request, url_for, send_from_directory, abort
from flask_cors import CORS
from datetime import datetime
import os
import uuid

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route('/', methods=['GET','POST'])
def analyze():
    url = "https://apis.openapi.sk.com/urbanbase/v1/space/analyzer"

    # user_img_path
    payload = "{\"image_path\":\"https://www.ikea.com/images/2-e4e271bd007a75af466351b6828af61c.jpg\"}"
    headers = {
        "accept": "application/json",
        "Content-Type": "json",
        "appKey": "XMGz6G5jzF5nybARW4cmY7fck4vpDiqg5u44kvRH"
    }

    response = requests.post(url, data=payload, headers=headers)

    # print('txt : ',response.text)
    # print(response.text.find('[{"label"'))
    # print(response.text.find('],"created_date'))
    start = response.text.find('[{"label"')
    end = response.text.find('],"created_date')
    result=response.text[start:end+1]
    # print(result.find('[{"label"'))
    # print(result.find('},{'))
    cut=result.find('},{')
    result=result[:cut+1]
    
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
    print(label, probability, description)
    
    
    ### dictionary
    data = {
        'label' : label,
        'probability' : probability,
        'description' : description
    }
    
    return render_template('api.html', data=data)

# <img src="{{ url_for('get_image', filename=image_filename) }}" alt="Image">
@app.route('/image/<path:filename>')
def get_image(filename):
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static')
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5500')