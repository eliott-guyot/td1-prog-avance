from django.shortcuts import render
from .models import Produit,Statut,Categorie
from django.http import HttpResponse, Http404


def home(request,param=None):
    if request.GET and request.GET["test"]:
        raise Http404
    return HttpResponse("Bonjour Monde!")

def aboutus(request):
    return HttpResponse("<h1>à propos de nous!</h1>")
def contactus(request):
    return HttpResponse("<h1>nous contacter!</h1>")

def ListProduits(request):
    prdts = Produit.objects.all()
    return HttpResponse(f"""
        <p>Mes produits sont :<p>
        <ul>
            <li>{prdts[0].intituleProd}</li>
            <li>{prdts[1].intituleProd }</li>
            <li>{prdts[2].intituleProd }</li>
        </ul>
    """)

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

def accueil(request,param):
    return HttpResponse("<h1>Hello " + param + " ! You're connected</h1>")
