from django.contrib import admin
from .models import Produit,Categorie,Statut,Rayon,Contenir

class ProduitAdmin(admin.ModelAdmin):
    model = Produit
    list_display = ["refProd", "intituleProd", "prixUnitaireProd", "dateDeFabrication", "categorie", "statut"]
    list_editable = ["intituleProd", "prixUnitaireProd", "dateDeFabrication"]
    radio_fields = {"statut": admin.VERTICAL}
    search_fields = ('intituleProd', 'dateDeFabrication')
    
admin.site.register(Produit, ProduitAdmin)

class ProduitInline(admin.TabularInline):
    model = Produit
    extra = 1 # nombre de lignes vides par défaut


class CategorieAdmin(admin.ModelAdmin):
    model = Categorie
    inlines = [ProduitInline]
admin.site.register(Categorie,CategorieAdmin)



admin.site.register(Statut)
admin.site.register(Rayon)
admin.site.register(Contenir)

