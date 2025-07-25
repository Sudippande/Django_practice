from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout ,authenticate,login
from django.http import HttpResponse

#password for test user is Sudip is Sudip$$$000

def index(request):
    #if user is anonimous who doesnot have login id or any thing than for him we will check like this
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'index.html')

def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # authenticate logic here...
    #     if username == username and password == password:
    #         return render(request,'index.html')  # or any success page
    #     else:
    #         return render(request, 'login.html', {'error': 'Invalid credentials'})
    # return render(request, 'login.html')  # This ensures GET request returns an HttpResponse

#another way is this
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html')
    return render(request,'login.html')
    
def logoutuser(request):
    logout(request)
    return redirect('/login')
