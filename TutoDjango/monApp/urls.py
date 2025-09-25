from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    path("home/", views.HomeView.as_view(),name='home'),
    path("aboutus", views.AboutView.as_view(), name="aboutus"),
    path("contactus", views.ContactView, name="contactus"),
    path("ListProduits", views.ListProduits, name="ListProduits"),
    path("ListStatut", views.ListStatut, name="ListStatut"),
    path("listeRayon", views.listeRayon, name="listeRayon"),

    path("ListCat", views.ListCat, name="ListCat"),
    path("home/<param>",views.HomeView.as_view() ,name='accueil'),
    path("produits/",views.ProduitListView.as_view(),name="lst_prdts"),
    path("produit/<pk>/" ,views.ProduitDetailView.as_view(), name="dtl_prdt"),
    path("Categories/" ,views.CategorieListView.as_view(), name="lst_cat"),
    path("Categorie/<pk>/" ,views.CategorieDetailView.as_view(), name="dtl_cat"),
    path("Statuts/" ,views.StatutListView.as_view(), name="lst_stt"),
    path("Statut/<pk>/" ,views.StatutDetailView.as_view(), name="dtl_stt"),
    path("Rayons/" ,views.RayonListView.as_view(), name="lst_rayon"),
    path("Rayon/<pk>/" ,views.RayonDetailView.as_view(), name="dtl_rayon"),
    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),
    path('email-sent/', views.EmailsentView, name='email-sent'),
    path("produit/",views.ProduitCreateView.as_view(), name="crt-prdt"),
    path("produit/<pk>/update/",views.ProduitUpdateView.as_view(), name="prdt-chng"),



]
