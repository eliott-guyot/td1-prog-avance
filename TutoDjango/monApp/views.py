from django.shortcuts import render

from django .http import HttpResponse
def home(request  ):
    return HttpResponse ("<h1>bonsoir<h1>")
def homeAv(request , param ):
    return HttpResponse ("<h1>"+param+"<h1>")
            

def aboutus(request):
    return HttpResponse("<h1>à propos de nous!</h1>")
def contactus(request):
    return HttpResponse("<h1>nous contacter!</h1>")

