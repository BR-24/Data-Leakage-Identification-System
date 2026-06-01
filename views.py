from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from bs4 import BeautifulSoup
from urllib import request

url2 = "https://matplotlib.org/tutorials/introductory/lifecycle.html#sphx-glr-tutorials-introductory-lifecycle-py"
url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"
html = request.urlopen(url)

doc =BeautifulSoup(html,"html.parser")
print(doc.find_all('pre'))
print("-------------")
for k in doc.find_all('pre'):
    print(str(k))
print("-------------")   
# Create your views here.
def home(request):

    return render(request,"home.html",{})

def app_login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')

    return render(request,"login.html",{})

def app_signup(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username,password=password,email=email)
        user.save()
        return redirect('login')

    return render(request,"signup.html",{})

def data_form(request):
    
    return render(request,"data_form.html",{})