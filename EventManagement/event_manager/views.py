from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def events(request):
    return render(request, 'events.html')

def about(request):
    return render(request, 'about.html')
