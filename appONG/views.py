from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def OqueONG (request):
    return render(request, 'OqueONG.html')

def OqueFaz (request):
    return render(request, 'OqueFaz.html')

def DoacoesONG (request):
    return render(request, 'DoacoesONG.html')
