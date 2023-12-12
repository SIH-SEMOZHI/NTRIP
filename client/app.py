from flask import Flask, request, render_template
import requests
import json
from Model import GNSSData
app = Flask(__name__, template_folder='templates')
cnt=0
@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/getLoc")
def getLoc():
    global cnt
    if cnt==10:
        cnt=0
    server_url = "http://127.0.0.1:8888/data"
    payload = {'type':'rover','step':cnt}
    try:
        response = requests.post(server_url, json=payload)
        response.raise_for_status()         
        x=GNSSData.from_dict(json.loads(response.text))
        cnt+=1
        return json.loads(response.text)
    
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with the server: {e}")
        return "Error communicating with the server."
@app.route("/dgnss")
def dgnss():
    server_url = "http://127.0.0.1:8008/dgnss/"
    payload = {'mount':'XXXXX'}
    try:
        response = requests.post(server_url, json=payload)
        response.raise_for_status()         
        return json.loads(response.text)
    
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with the server: {e}")
        return "Error communicating with the server."

if __name__ == "__main__":
    app.run(debug=True, port=8080)
