from django.shortcuts import render

# Create your views here.

def cdn_Bootstrap(request):
    return render(request,'cdn_Bootstrap.html')