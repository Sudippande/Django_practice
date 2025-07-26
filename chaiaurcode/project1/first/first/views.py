from django.http import HttpResponse ,HttpResponseRedirect# type: ignore
from django.shortcuts import render ,redirect # type: ignore
from .forms import userForm


def index(request):
    return render(request,'index.html')
def service(request):
    return render(request,"service.html")
def userform(request):
    final=0
    fn=userForm()
    data={'form':fn}
    try:
        
        if request.method=="POST":
            username=request.POST['username']
            pwd=request.POST['password']
            final=username+" "+pwd
        data={
            'username':username,
            'pwd':pwd,
            'output':final
        }
        if username=='admin' and pwd=='admin':
            return redirect('/')
        
    except:
        pass
    return render(request,'userform.html',data)

def header(request):
    return render(request,'header.html')
def aboutus(request):
    return render(request,'aboutus.html')
def submit_form(request):
    return render(request,'submit_form.html')