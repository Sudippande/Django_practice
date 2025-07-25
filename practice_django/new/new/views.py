from django.shortcuts import render
from django.http import HttpRequest

def index(request):
    # data={
    #     'p':'Mula ko Sag',
    #     'numbers':[9,2],
    #     'name':[{'nam':'sudip','age':'23'},
    #         {'nam':'ram','age':'66'}]
    # }
    return render(request, 'index.html')

def course(request):
    return render(request,'course.html')

def courseDetail(request,courseid):
    return render(request,courseid)

def header(request):
    return render(request,'header.html')
def base(request):
    return render(request,'base.html')
def aboutus(request):
    return render(request,'aboutus.html')