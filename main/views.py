from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    context = {
        'title': 'Home - Main page',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'About us',
    }

    return render(request, 'main/about.html', context)

def contact(request):
    context = {
        'title': 'Contact us',
    }

    return render(request, 'main/contact.html', context)


def services(request):
    context = {
        'title': 'Services',
    }

    return render(request, 'main/services.html', context)