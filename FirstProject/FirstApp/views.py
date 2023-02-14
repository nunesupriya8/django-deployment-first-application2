from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.<html>
print("wlecome/ url is requested and display()is exicuted");
def display(request):
 ss='''
  <center>
  <h2 style="color:blue;">
  hello user welcome to django first project
  </h2>
  <hr/>
  </center>
  ''';
 return HttpResponse(ss);
 
def hello(request):
 s='''
 <html>
 <head>
       <title>hello webpage</title>
        <style>
            h1{
              color:blue;
              width:90%;
            }
            h2{
              color:violet;
              width:70%;
            }
            h3{
              color:blue;
              width:60%;
            }
           h1,h2,h3{
              background-color:lightblue;
              border:2px solid brown;
            }
        </style>
 </head>
 <body>
    <center>
       <h1>hello user..!!</h1>
       <hr color="blue" width="90%"/>
       <h2>welcome to django</h2>
       <hr color="brown" width="80%"/>
       <h3>have a nice day..!!!</h3>
       <hr color="red" width="70%"/>
    </center> 
 </body>
 </html> 
 ''';
 return HttpResponse(s);
import time;
def senddatetime(request):
 print('dtime/ url is requested and senddatetime() is executed');
 ct=time.ctime()
 print('client request date & time on server ::',ct);
 ss='''
 <html>
 <head>
 <title>date-time web-page</title>
 <style>
 h1{
 color:blue;
 width:90%;
 }
 h2{
 color:green;
 width:80%;
 }
 h3{
 color:red;
 width:70%;
 }
 h1,h2,h3{
  background-color:lightgreen;
  border:2px solid brown;
 }
 </style>
 </head>
 <center>
 <h1>welcome to django-user..!!!</h1>
 <hr color='brown' width='90%'>
 <h2>server-date&time::</h2>
 <hr color='brown' width='80%'>
 <h3>''',ct,'''</h3>
 <hr color='brown' width='70%'>
 </center>
 </body>
 </html>
 ''';
 return HttpResponse(ss);
def demo(request):
 print("multiple-request-urls same response");
 htmldata='''
 <center>
 <h1>welcome demo user!!!</h1>
 <hr/>
 <h2>this is same ooutput for different urls</h2>
 <hr/>
 <h3>have a great day...</h3>
 </center>
 ''';
 return HttpResponse(htmldata);
def homepage(request):
 htmldata='''
 <center>
 <h1>welcome to default home page..!!!</h1>
 <hr/>
 <h2>request page is not found..!!</h2>
 <hr/>
 <h3>plz try another url or linnk!!</h3>
 <hr/>
 </center>
 ''';
 return HttpResponse(htmldata);
 