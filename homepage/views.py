from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage/homepage.html')


def about(request):
    return render(request, 'homepage/about.html')

