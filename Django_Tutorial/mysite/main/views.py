from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1> Project! </h1>")

def views(response):
    return HttpResponse("<h1> Project views page </h1>")

def sign_in(response):
    return HttpResponse("<h1> Sign in page </h1>")
