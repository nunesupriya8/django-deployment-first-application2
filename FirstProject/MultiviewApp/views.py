from django.shortcuts import render
from django.http import HttpResponse

#Create your views here.
def f1(request):
 return HttpResponse("<h1>good morning user.!!! have a nice day</h1><hr/>");
def f2(request):
 return HttpResponse("<h1>good afternoon user!!! hope u r doing good</h1><hr/>");
def f3(request):
 return HttpResponse("<h1>good evening user!!! how was ur day</h1><hr/>")
