from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    path("home/", views.HomeView.as_view()),
    path("aboutus", views.AboutView.as_view(), name="aboutus"),
    path("contactus", views.ContactView.as_view(), name="contactus"),
    path("ListProduits", views.ListProduits, name="ListProduits"),
    path("ListStatut", views.ListStatut, name="ListStatut"),
    path("listeRayon", views.listeRayon, name="listeRayon"),

    path("ListCat", views.ListCat, name="ListCat"),
    path("home/<param>",views.HomeView.as_view() ,name='accueil'),
    path("produits/",views.ProduitListView.as_view()),
    path("produit/<pk>/",views.ProduitDetailView.as_view()),
    

]
