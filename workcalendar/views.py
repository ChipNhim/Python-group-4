from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "layout/login.html")

def dashboad(request):
    return render(request, "dashboard/index.html")