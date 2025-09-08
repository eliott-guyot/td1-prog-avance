from django.contrib import admin
from .models import Produit,Categorie,Statut,Rayon,Contenir

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('intituleProd', 'prixUnitaireProd')
admin.site.register(Produit, ProduitAdmin)

admin.site.register(Categorie)
admin.site.register(Statut)
admin.site.register(Rayon)
admin.site.register(Contenir)

class ProduitInline(admin.TabularInline):
    model = Produit
    extra = 1 # nombre de lignes vides par défaut

class CategorieAdmin(admin.ModelAdmin):
    model = Categorie
    inlines = [ProduitInline]