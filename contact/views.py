from django.shortcuts import render
from django.http import HttpResponse
from contact.models import PeopleInfo

# Create your views here.

def index(request):
    return render(request, 'demo.html')


def home(request):
    return HttpResponse("Home")

def movie(request):
    return HttpResponse("movie")


def save_data(request):
    username = request.POST.get("username")
    passwd = request.POST.get("passwd")
    PeopleInfo.objects.create(name=username, password=passwd)
    print(username, passwd)
    return HttpResponse("数据保存成功")