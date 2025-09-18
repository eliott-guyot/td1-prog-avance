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
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        if self.kwargs.get('param')!=None:
            context['titreh1'] = "Hello DJANGO "+self.kwargs.get('param')
        else:
            context['titreh1'] = "Hello DJANGO"
        return context
    
class AboutView(TemplateView):
    template_name = "monApp/page_home.html"
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us..."
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name)
    

class ContactView(TemplateView):
    template_name = "monApp/page_home.html"
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['titreh1'] = "contact us..."
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"
    def get_queryset(self ) :
        return Produit.objects.order_by("prixUnitaireProd")
    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context
    
class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"
    def get_context_data(self, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context