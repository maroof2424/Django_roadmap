from django.shortcuts import render,HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("Hello This is running")


def home(request):
    return render(request,"pages/home.html")