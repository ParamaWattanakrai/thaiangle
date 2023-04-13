from django.shortcuts import render

def home(request):
    return render(request, 'app_general/index.html')

def about(request):
    return render(request, 'app_general/about.html')