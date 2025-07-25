from django.shortcuts import render,redirect
from datetime import datetime
from myapp.models import Contact,Signup
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout ,authenticate,login
from django.http import HttpResponse

#password for test user is Sudip is Sudip$$$000



# Create your views here.
def index(request):
    #if user is anonimous who doesnot have login id or any thing than for him we will check like this
    # if request.user.is_anonymous:
    #     return redirect('/login')
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')
    # return HttpResponse("this is a about page sudip")


def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        file=request.POST.get('file')
        number=request.POST.get('number')
        feedback=request.POST.get('feedback')
        contact=Contact(name=name,email=email,file=file,number=number,feedback=feedback,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent !")
    return render(request,'contact.html')
    # return HttpResponse("this is a contact us section")



def services(request):
    # return HttpResponse("this is a service page")
    return render(request,'services.html')



def signup(request):
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        address=request.POST.get('address')
        email=request.POST.get('email')
        password=request.POST.get('password')
        conform=request.POST.get('conform')
        signup=Signup(fullname=fullname,address=address,email=email,password=password,conform=conform,date=datetime.today())
        signup.save()

    return render(request,'signup.html')
def image1(request):
    return render(request,'image1.html')
def buynow(request):
    return render(request,"buynow.html")
def cart(request):
    return render(request,'cart.html')




def login(request):
    # if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # authenticate logic here...
#     #     if username == username and password == password:
#     #         return render(request,'index.html')  # or any success page
#     #     else:
#     #         return render(request, 'login.html', {'error': 'Invalid credentials'})
#     # return render(request, 'login.html')  # This ensures GET request returns an HttpResponse

# #another way is this
#         user=authenticate(username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('/')
#         else:
#             return render(request,'login.html')
    return render(request,'login.html')
    
def logout(request):
    logout(request)
    return redirect('/login')


