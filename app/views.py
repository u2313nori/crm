from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    """メニュー"""
    return render(request, 'app/index.html')
