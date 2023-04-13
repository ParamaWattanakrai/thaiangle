from django.shortcuts import render

def anatomy(request):
    return render(request, 'app_anatomy/anatomy.html')