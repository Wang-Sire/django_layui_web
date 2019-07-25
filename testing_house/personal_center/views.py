import json
from .models import *
from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator


def home_page(request):
    return render(request, 'home_page.html', locals())


def my_news(request):
    return render(request, 'my_news.html', locals())
