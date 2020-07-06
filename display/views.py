from django.shortcuts import render
import requests
import json
# Create your views here.


def login(request):
    return render(request, 'login.html')

def signin(request):
    return render(request,'signin.html')


def submitUser(request):
    email = request.GET['emailid']
    password = request.GET['pass']
    name = request.GET['name']

    print(email,password,name,"this is me")

    url = "http://localhost:6269/applogin/"

    payload = {"email":email, "password":password, "name":name}
    payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.text
    return render(request, 'temp.html', {'data':data})



def getUser(request):
    email = request.GET['emailid']
    password = request.GET['pass']
    # name = request.GET['name']

    print(email,password,"this is me")

    url = "http://localhost:6269/applogin/"

    payload = {"email":email, "password":password}
    payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text
    return render(request, 'temp.html', {'data':data})



