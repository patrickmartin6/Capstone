from django.shortcuts import render


def index(request): #creating the url connection for the home page
    return render(request, 'index.html', {})
def about(request):#creating the url connection for the help page
    return render(request, 'about.html', {})
def registration(request):#creating the url connection for the help page
    return render(request, 'registration.html', {})
def websocket(request):#creating the url connection for the help page
    return render(request, 'websocket.html', {})
def passwordreset(request):#creating the url connection for the help page
    return render(request, 'passwordreset.html', {})

