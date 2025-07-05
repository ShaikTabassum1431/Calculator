from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    result=None
    error=None
    if request.method=="POST":
        a=int(request.POST.get('Num1'))
        b=int(request.POST.get('Num2'))
        c=request.POST.get('Op') 
        if c=="add":
           result=a+b
        elif c=="sub":
            result=abs(a-b) 
        elif c=="mul":
            result=a*b 
        elif c=="div":
            if a!=0:
             result=a//b 
            else:
                result=0
        else:
            return render(request,'home.html',{'error':'error'})
        #return render(request,'home.html',{'result':result})
        return redirect('hello',result)
    return render(request,'home.html')
def hello(request,result):
    return render(request,'result.html',{'result':result})
