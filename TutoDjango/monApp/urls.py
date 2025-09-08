from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home ,name='home'),
    path('homeAv/<param>',views.homeAv ,name='homeAv'),
    path("aboutus", views.aboutus, name="aboutus"),
    path("contactus", views.contactus, name="contactus"),
    path("ListProduits", views.ListProduits, name="ListProduits"),
    path("ListStatut", views.ListStatut, name="ListStatut"),
    path("ListStatut", views.ListStatut, name="ListStatut"),

]
