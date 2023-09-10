from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'landingpage/pages/home.html')

def coffee(request):
    return render(request,'landingpage/pages/coffee.html')

def tea(request):
    return render(request,'landingpage/pages/tea.html')

def milk(request):
    return render(request,'landingpage/pages/milk.html')