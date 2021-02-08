from flask import Flask, jsonify
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from flask_cors import CORS
import shlex, subprocess

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

def default(o):
    if hasattr(o, 'to_json'):
        return o.to_json()
    raise TypeError(f'Object of type {o.__class__.__name__} is not JSON serializable')


@app.route('/')
def hello_world():
    return "Hello World!"

def get_token(user_name, password):
    url = "https://api.gravity.networks.dell.com/v1/login" 
    r = requests.get(url, headers = {"Username": user_name, "Password":password}, verify=False)
    resp = r.json()
    token = resp['token'];

    return   token

@app.route('/logintest')
def logintest():
    return get_token("sarath_chintapatla@apac.dell.com", "Welcome@123")


@app.route('/loginfo')
def log_info():

    cmd = '''curl -k -X GET "https://api.gravity.networks.dell.com/v1/login" -H "accept: application/json" -H "Username:sarath_chintapatla@apac.dell.com" -H "Password:Welcome@123"'''
    args = shlex.split(cmd)
    process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    r = {
        "response": json.dumps(stdout)
    }
    return   jsonify(r)

if __name__ == '__main__':
    app.run()