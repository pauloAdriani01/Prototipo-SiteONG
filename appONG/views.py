from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def loginpage (request):
    return render(request, 'loginpage.html')
