from django.shortcuts import render 
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

data={}

@csrf_exempt
def record(request):
    if request.method == 'POST':
        try:
            received_data = json.loads(request.body)
            print(received_data)
            data[received_data["mountPoint"]]=received_data
            print(data)
            return JsonResponse(received_data)

        except json.JSONDecodeError as e:
            return JsonResponse({'error': f'Error decoding JSON: {e}'})
    else:
        return JsonResponse({'error': 'Invalid request method. Use POST.'})
@csrf_exempt
def process(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)  
            print(payload)
            return JsonResponse(data[payload["mount"]])
        except json.JSONDecodeError as e:
            return JsonResponse({'error': f'Error decoding JSON: {e}'})
    else:
        return JsonResponse({'error': 'Invalid request method. Use POST.'})