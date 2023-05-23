from django.shortcuts import render
from django.http import HttpResponse

# This function serves a view
def index(response):
    return HttpResponse("<h1>tech with tim!</h1>")

def v1(response):
    return HttpResponse("<h1>view 1 </h1>")