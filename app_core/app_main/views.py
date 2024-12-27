from django.shortcuts import render

def home(request):
    return render(request, 'app_main/home.html')

def about(request):
    return render(request, 'app_main/about.html')
