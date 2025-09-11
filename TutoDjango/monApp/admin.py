from django.contrib import admin
from .models import Produit,Categorie,Statut,Rayon,Contenir


class ProduitFilter(admin.SimpleListFilter):
    title = 'filtre produit'
    parameter_name = 'custom_status'
    def lookups(self, request, model_admin) :
        return (
        ('OnLine', 'En ligne'),
        ('OffLine', 'Hors ligne'),
        )
    def queryset(self, request, queryset):
        if self.value() == 'OnLine':
            return queryset.filter(statut=1)
        if self.value() == 'OffLine':
            return queryset.filter(statut=0)


class ProduitAdmin(admin.ModelAdmin):
    model = Produit
    list_display = ["refProd", "intituleProd", "prixUnitaireProd", "dateDeFabrication", "categorie", "statut"]
    list_editable = ["intituleProd", "prixUnitaireProd", "dateDeFabrication","statut"]
    radio_fields = {"statut": admin.VERTICAL}
    search_fields = ('intituleProd', 'dateDeFabrication')
    list_filter = (ProduitFilter,)
    date_hierarchy = 'dateDeFabrication'

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

