from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
# views.py
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home(request):
    return HttpResponse('Hello World')
    
@csrf_exempt    
def login(request):
    print('Request: ', request)
    print('Request method: ', request.method)
    if request.method == "POST":
        print('Login form post method successfull', request.body)
        ob = json.loads(request.body)
        print('Login Object data: ', ob)
        print('Email: ', ob['email'])
        print('Password: ', ob['password'])
        return HttpResponse('Login form post method successfull')
    return HttpResponse('Login Page')

@csrf_exempt
def addCustomer(request):
    if(request.method == 'POST'):
        print('Add Customer Data in Binary Format: ', request.body)
        cust = json.loads(request.body)
        print('Customer Data in Dictniory format:', cust)
        # return HttpResponse('Add Customer Data got Successfully')
        return JsonResponse({'message': 'Add Customer Data got Successfully', 'data': cust})
        
    return HttpResponse('Hello... This is Add Customer Page')
