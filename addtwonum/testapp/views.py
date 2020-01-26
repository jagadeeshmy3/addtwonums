from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request,'index.html')

def result(request):
    t1 = int(request.GET["t1"])
    t2 = int(request.GET["t2"])
    result = t1+t2
    # res = str(result)
    return render(request,'result.html',{'res':result})
