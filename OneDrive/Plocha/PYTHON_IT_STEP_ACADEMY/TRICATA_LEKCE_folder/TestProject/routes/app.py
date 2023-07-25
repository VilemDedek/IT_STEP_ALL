from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/about')
def about():
    return "This is the About page"

@app.route('/contact')
def contact():
    return "This is a contact page"

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'GET':
        return 'This is a GET request.'
    elif request.method == 'POST':
        data = request.json
        print("The data is \n", data)
        return 'This is a POST request'
    else:
        return 'Invalid reguest'
    
#############################xx
import requests
# zde nemáme decorátor protože nespojujeme FUNKCIONALITU  s aplikací
def send_post_request(url, data):
    response = requests.post(url, json=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        return None
    
if __name__ == '__main__':

    app.run()



if __name__ == '__main__': # vše co je pod ifem se spustí jakos script
    app.run()