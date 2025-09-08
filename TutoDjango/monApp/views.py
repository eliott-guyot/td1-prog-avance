from django.shortcuts import render
from .models import Produit,Statut,Categorie
from django .http import HttpResponse

def home(request  ):
    return HttpResponse ("<h1>bonsoir<h1>")
def homeAv(request , param ):
    return HttpResponse ("<h1>"+param+"<h1>")
            

def aboutus(request):
    return HttpResponse("<h1>à propos de nous!</h1>")
def contactus(request):
    return HttpResponse("<h1>nous contacter!</h1>")

def ListProduits(request):
    prdts=Produit.objects.all()
    html=f" <h1>Produit</h1>"
    html += "<ul>"
    for p in prdts:
        html += f"<li>{p.intituleProd}</li>"
    html += "</ul>"
    return HttpResponse(html)

def ListStatut(request):
    stt=Statut.objects.all()
    html=f" <h1>Produit</h1>"
    html += "<ul>"
    for p in stt:
        html += f"<li>{p.libelléStatut}</li>"
    html += "</ul>"
    return HttpResponse(html)

def ListCat(request):
    cat=Categorie.objects.all()
    html=f" <h1>Produit</h1>"
    html += "<ul>"
    for p in cat:
        html += f"<li>{p.nomCat}</li>"
    html += "</ul>"
    return HttpResponse(html)