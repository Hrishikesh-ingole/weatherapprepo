from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/weatherapp', methods=['POST','GET'])
def get_details():
    url = 'http://api.openweathermap.org/data/2.5/weather'
    parmas = {
        'q' : request.form.get('city'),
        'matric' : request.form.get('units'),
        'appid' : request.form.get('appid')
    }
    response =  requests.get(url, parmas)
    data = response.json()
    return f'data: {data}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)