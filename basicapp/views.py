from django.shortcuts import render, redirect, HttpResponse, get_object_or_404



def home(request):
    return render(request, 'home.html')

def system(request):
    return render(request, 'system.html')
