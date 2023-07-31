from django.shortcuts import render

# Create your views here.
def baseview(request):
    return render(request,'base.html')


def indexview(request):
    return render(request,'index.html')

def registerview(request):
    return render(request,'register.html')


def loginview(request):
    return render(request,'login.html')