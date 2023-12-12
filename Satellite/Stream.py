from flask import Flask,request
import requests
from data import *
import json
app = Flask(__name__)

@app.route('/data',methods=['POST'])
def handle_station():
    data=(request.get_json())
    if(data["type"]=='rover'):
        print(client[int(data["step"])].long)
        return client[int(data["step"])].to_dict()

    if(data["type"]=='base'):
        print(reference[int(data["step"])].long)
        return reference[int(data["step"])].to_dict()
@app.route('/')
def home():
    print([ i.to_dict() for i in reference])
    return "Hello from Satellite!"

if __name__ == "__main__":
    app.run(port=8888)
