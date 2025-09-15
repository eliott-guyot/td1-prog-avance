from django.shortcuts import render
from .models import Produit,Statut,Categorie,Rayon
from django.http import HttpResponse, Http404
from django.views.generic import *


def aboutus(request):
    return render(request, 'monApp/about.html')

def contactus(request):
    return render(request, 'monApp/contactus.html')

def ListProduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html',{'prdts': prdts})

def ListStatut(request):
    stt=Statut.objects.all()
    return render(request, 'monApp/listStatut.html',{'stt': stt})
def listeRayon(request):
    rayon=Rayon.objects.all()
    return render(request, 'monApp/listeRayon.html',{'rayon': rayon})


def ListCat(request):
    cat=Categorie.objects.all()
    return render(request, 'monApp/listeCat.html',{'cat': cat})

def accueil(request,param):
    return HttpResponse("<h1>Hello " + param + " ! You're connected</h1>")



class HomeView(TemplateView):
    template_name = "monApp/page_home.html"
    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
class AboutView(TemplateView):
    template_name = "monApp/page_home.html"
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us..."
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name)