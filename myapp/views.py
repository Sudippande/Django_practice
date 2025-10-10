from django.shortcuts import render
from myapp.models import Table
from myapp.forms import TableForm
from django.shortcuts import get_object_or_404, redirect

def Delete(request, id):
    c = get_object_or_404(Table, id=id)  # safer way to fetch
    c.delete()
    return redirect('index')  # redirect to your data listing page


# Create your views here.
def index(request):
    a=Table.objects.all()
    context={
        'for':a
    }
    return render(request,'index.html',context)

def form_data(request):
    if request.method=='POST':
        form=TableForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=TableForm()
    return render(request,'form_data.html',{'form':form})

def about(request):
    return render(request,'about.html')

def Edit(request,id):
    b=get_object_or_404(Table,id=id)
    if request.method== "POST":
        form=TableForm(request.POST,request.FILES, instance=b)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form=TableForm(instance=b)
    return render(request,'Edit.html',{'form':form})

def Delete(request,id):
    c=get_object_or_404(Table,id=id)
    if request.method=='POST':
        c.delete()
        return redirect('index')
    return render(request,'confirm_delete.html',{'obj':c})
