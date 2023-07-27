from django.shortcuts import render

# Create your views here.
def baseview(request):
    return render(request,'base.html')


def indexview(request):
    return render(request,'index.html')

def authview(request):
    return render(request,'authentication.html')