from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models import *
from django.core.mail import send_mail
from django.conf import settings
from .forms import SendLetter

def index(request):
    carousel = Carousel.objects.all()
    sh_products = Short_products.objects.all()
    nums = Nums.objects.first()
    footer = Footer.objects.all()
    pluses = Pluses.objects.all()

    context = {
        'title': 'Home - Main page',
        'carousel': carousel,
        'sh_products': sh_products,
        'nums': nums,
        'footer': footer,
        'pluses': pluses,
    }

    return render(request, 'main/index.html', context)

def about(request):
    about_us = Info.objects.all()
    team_desc = TeamInfo.objects.all()
    team = Team.objects.all()

    context = {
        'title': 'About us',
        'about_us': about_us,
        'team_desc': team_desc,
        'team': team,
    }

    return render(request, 'main/about.html', context)

def contact(request):
    if request.method == 'POST':
        form = SendLetter(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_name = f"{first_name} {last_name}"
            sender_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.EMAIL_HOST_USER]

            # Compose the email
            email_body = f"""
            From: {full_name} <{email}>
            Subject: {subject}
            
            Message:
            {message}
            """

            # Send the email
            send_mail(
                subject='Website Contact Form Submission',
                message=email_body,
                from_email=sender_email,
                recipient_list=recipient_list,
                fail_silently=False,
            )

            # Redirect to a success page
            return redirect('success')
    else:
        form = SendLetter()

    return render(request, 'main/contact.html', {'form': form})

def services(request):
    services = Services.objects.all()

    context = {
        'title': 'Services',
        'services': services,
    }

    return render(request, 'main/services.html', context)
