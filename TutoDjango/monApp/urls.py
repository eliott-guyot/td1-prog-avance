from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    path("home/", views.HomeView.as_view()),
    path('home/<param>',views.home ,name='home'),
    path("aboutus", views.aboutus, name="aboutus"),
    path("contactus", views.contactus, name="contactus"),
    path("ListProduits", views.ListProduits, name="ListProduits"),
    path("ListStatut", views.ListStatut, name="ListStatut"),
    path("listeRayon", views.listeRayon, name="listeRayon"),

    path("ListCat", views.ListCat, name="ListCat"),
    path("home/<param>",views.accueil ,name='accueil'),
    path("home", TemplateView.as_view(template_name="monApp/page_home.html")),

]
