from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path('home/<param>',views.home ,name='home'),
    path("aboutus", views.aboutus, name="aboutus"),
    path("contactus", views.contactus, name="contactus"),
    path("ListProduits", views.ListProduits, name="ListProduits"),
    path("ListStatut", views.ListStatut, name="ListStatut"),
    path("listeRayon", views.listeRayon, name="listeRayon"),

    path("ListCat", views.ListCat, name="ListCat"),
    path("home/<param>",views.accueil ,name='accueil'),

]
