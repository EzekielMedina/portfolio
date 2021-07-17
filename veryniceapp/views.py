from django.shortcuts import render, redirect
from .models import *


# def index(request):
#     return render(request, 'main.html')


def learnpage(request):
    return render(request, 'learnabout.html')


def clothingpage(request):
    return render(request, 'clothingpage.html')


def resumepage(request):
    return render(request, 'resume.html')


def createmess(request):
    Message.objects.create(
        usermessage=request.POST['mess']
    )
    return redirect('/')


def index(request):
    context = {
        'all_messages': Message.objects.all()
    }
    return render(request, 'main.html', context)

# Create your views here.
