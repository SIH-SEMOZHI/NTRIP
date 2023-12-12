from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json
from .models import GNSSData,Data
CRLONG = 76.936108
CRLAT= 11.01613
cnt = 0
def home(request):
    return HttpResponse("Hello from the Server!")
def satellite(request):
    global cnt
    if cnt == 10:
        cnt = 0
    server_url = "http://127.0.0.1:8888/data"
    payload = {'type': 'base', 'step': cnt}
    try:
        response = requests.post(server_url, json=payload)
        response.raise_for_status()
        data = json.loads(response.text)
        FormatX=calculateError(GNSSData.from_dict(data))
        cnt += 1
        push(FormatX.to_dict())
        return JsonResponse(FormatX.to_dict())
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with the server: {e}")
        return JsonResponse({"error": "Error communicating with the server."})

def calculateError(gnss):
    d=Data()
    d.lat=gnss.lat
    d.long=gnss.long
    d.time=gnss.time
    d.satID=gnss.satID
    d.dlat=gnss.lat-CRLAT
    d.dlong=gnss.long-CRLONG
    d.mountPoint="XXXXX"
    return d
    

def push(data):
    server_b_url = "http://127.0.0.1:8008/record/"
    try:
        response = requests.post(server_b_url, json=data)
        response.raise_for_status()
        return JsonResponse({'message': 'Data sent successfully'})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'Error sending data: {e}'})
