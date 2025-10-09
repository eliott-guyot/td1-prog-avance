from django.shortcuts import get_object_or_404, render
from django.forms import BaseModelForm
from monApp.forms import ContactUsForm, ContenirForm, ProduitForm,CategorieForm,StatutForm,RayonForm
from .models import Contenir, Produit,Statut,Categorie,Rayon
from django.http import HttpResponse, Http404
from django.views.generic import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.db.models import Count, Prefetch
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

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
    


    
class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"
    def get_queryset(self):
        # Surcouche pour filtrer les résultats en fonction de la recherche
        # Récupérer le terme de recherche depuis la requête GET
        query = self.request.GET.get('search')
        if query:
            return Produit.objects.filter(intituleProd__icontains=query).select_related('categorie').select_related('statut')
        # Si aucun terme de recherche, retourner tous les produits
        # Charge les catégories en même temps
        return Produit.objects.select_related('categorie').select_related('statut')
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
    
class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "cat"
    def get_queryset(self):
        # Surcouche pour filtrer les résultats en fonction de la recherche
        # Récupérer le terme de recherche depuis la requête GET
        query = self.request.GET.get('search')
        if query:
            return Categorie.objects.filter(nomCat__icontains=query)
        # Si aucun terme de recherche, retourner tous les produits
        # Charge les catégories en même temps
        return Categorie.objects.all
    def get_context_data(self, **kwargs):
        context = super(CategorieListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes catégories"
        return context


class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    context_object_name = "cat"
    def get_queryset(self):
        return Categorie.objects.annotate(nb_produits=Count('produits'))
    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        context['prdts'] = self.object.produits.all()
        return context
    
class StatutListView(ListView):
    model = Statut
    template_name = "monApp/list_Statut.html"
    context_object_name = "stt"

    def get_context_data(self, **kwargs):
        context = super(StatutListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes statuts"
        return context
    

class StatutDetailView(DetailView):
    model = Statut
    template_name = "monApp/detail_Statut.html"
    context_object_name = "stt"
    def get_queryset(self):
        return Statut.objects.annotate(nb_produits=Count('produits'))

    def get_context_data(self, **kwargs):
        context = super(StatutDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail des statuts"
        context['prdts'] = self.object.produits.all()

        return context
    

class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/list_Rayon.html"
    context_object_name = "ryns"
    def get_queryset(self):
        # Surcouche pour filtrer les résultats en fonction de la recherche
        # Récupérer le terme de recherche depuis la requête GET
        query = self.request.GET.get('search')
        if query:
            return Rayon.objects.filter(nomRayon__icontains=query)
        # Si aucun terme de recherche, retourner tous les produits
        # Charge les catégories en même temps
        return Rayon.objects.all()
    def get_context_data(self, **kwargs):
        context = super(RayonListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes rayons"
        ryns_dt = []
        for rayon in context['ryns']:
            total = 0
            for contenir in rayon.contenir_rayon.all():
                total += contenir.nomprod.prixUnitaireProd * contenir.qte
                ryns_dt.append({'rayon': rayon,'total_stock': total})
        context['ryns_dt'] = ryns_dt
        return context

class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_Rayon.html"
    context_object_name = "ray"
    def get_context_data(self, **kwargs):
        context = super(RayonDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"
        prdts_dt = []
        total_rayon = 0
        total_nb_produit = 0
        for contenir in self.object.contenir_rayon.all():
            total_produit = contenir.nomprod.prixUnitaireProd * contenir.qte
            prdts_dt.append({ 'produit': contenir.nomprod,
            'qte': contenir.qte,
            'prix_unitaire': contenir.nomprod.prixUnitaireProd,
            'total_produit': total_produit} )
            total_rayon += total_produit
            total_nb_produit += contenir.qte
        print(prdts_dt)
        print('prdts_dt')
    
        context['prdts_dt'] = prdts_dt
        context['total_rayon'] = total_rayon
        context['total_nb_produit'] = total_nb_produit
        return context            
class ConnectView(LoginView):
    template_name = 'monApp/page_login.html'
    def post(self, request, **kwargs):
        lgn = request.POST.get('username', False)
        pswrd = request.POST.get('password', False)
        user = authenticate(username=lgn, password=pswrd)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'monApp/page_home.html', {'param': lgn, 'message': "You're connected"})
        else:
            return render(request, 'monApp/page_register.html')

class RegisterView(TemplateView):
    template_name = 'monApp/page_register.html'
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, 'monApp/page_login.html')
        else:
            return render(request, 'monApp/page_register.html')
class DisconnectView(TemplateView):
    template_name = 'monApp/page_logout.html'
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)
    
def ContactView(request):
    titreh1 = "Contact us !"
    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MonProjet Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@monprojet.com'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request, "monApp/page_home.html",{'titreh1':titreh1, 'form':form})

def EmailsentView(request):
    return render(request,"monApp/email-sent.html")


def ProduitCreate(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            prdt = form.save()
            return redirect('dtl_prdt', prdt.refProd)
    else:
        form = ProduitForm()
    return render(request, "monApp/create_produit.html", {'form': form})


class ProduitCreateView(CreateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/create_produit.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)
    
class ProduitUpdateView(UpdateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/update_produit.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)
    
def ProduitUpdate(request, id):
    prdt = Produit.objects.get(id=id)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=prdt)
        if form.is_valid():
            # mettre à jour le produit existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du produit que nous venons de mettre à jour
            return redirect('dtl_prdt', prdt.refProd)
    else:
        form = ProduitForm(instance=prdt)
    return render(request,'monApp/update_produit.html', {'form': form})

class ProductDeleteView(DeleteView):
    model = Produit
    template_name = "monApp/delete_produit.html"
    success_url = reverse_lazy('lst_prdts')

def produit_delete(request, id):
    prdt = Produit.objects.get(id=id) # nécessaire pour GET et pour POST
    if request.method == 'POST':
        # supprimer le produit de la base de données
        prdt.delete()
        # rediriger vers la liste des produit
        return redirect('lst_prdts')
    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement
    return render(request, 'monApp/delete_produit.html', {'object': prdt})






class CategorieCreateView(CreateView):
    model = Categorie
    form_class=CategorieForm
    template_name = "monApp/create_categorie.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        cat = form.save()
        return redirect('dtl_cat', cat.idCat)
    
class CategorieUpdateView(UpdateView):
    model = Categorie
    form_class=CategorieForm
    template_name = "monApp/update_categorie.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        cat = form.save()
        return redirect('cat-chng', cat.idCat)
    

class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = "monApp/delete_categorie.html"
    success_url = reverse_lazy('lst_cat')





class StatutCreateView(CreateView):
    model = Statut
    form_class=StatutForm
    template_name = "monApp/create_statut.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        stt = form.save()
        return redirect('dtl_stt', stt.idStatut)
    
class StatutUpdateView(UpdateView):
    model = Statut
    form_class=StatutForm
    template_name = "monApp/update_statut.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        stt = form.save()
        return redirect('stt-chng', stt.idStatut)
    

class StatutDeleteView(DeleteView):
    model = Statut
    template_name = "monApp/delete_statut.html"
    success_url = reverse_lazy('lst_stt')



class RayonCreateView(CreateView):
    model = Rayon
    form_class=RayonForm
    template_name = "monApp/create_rayon.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        ray = form.save()
        return redirect('dtl_ray', ray.idRayon)
    

class RayonUpdateView(UpdateView):
    model = Rayon
    form_class=RayonForm
    template_name = "monApp/update_rayon.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        ray = form.save()
        return redirect('ray-chng', ray.idRayon)
    

class RayonDeleteView(DeleteView):
    model = Rayon
    template_name = "monApp/delete_rayon.html"
    success_url = reverse_lazy('lst_rayon')

@login_required(login_url='/monApp/login/')
def my_view(request):
    return render(request, 'my_template.html')

# Ajout du décorateur login_required à une CBV
@method_decorator(login_required, name='dispatch')
class MyView(TemplateView):
    template_name = 'my_template.html'

class MyView(TemplateView):
    template_name = 'my_template.html'
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class ContenirCreateView(CreateView):
    model = Contenir
    form_class = ContenirForm
    template_name = "monApp/create_contenir.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        rayon = get_object_or_404(Rayon, pk=self.kwargs['pk'])
        produit = form.cleaned_data.get('nomprod')
        qte = form.cleaned_data.get('qte')

        contenir, created = Contenir.objects.get_or_create(
            nomprod=produit,
            nomRayon=rayon,
            defaults={'qte': qte}
        )
        if not created:
            contenir.qte = qte
            contenir.save()

        return redirect('dtl_rayon', pk=rayon.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ray'] = get_object_or_404(Rayon, pk=self.kwargs['pk'])
        return context
    
class ContenirUpdateView(UpdateView):
    model = Contenir
    form_class = ContenirForm
    template_name = "monApp/update_contenir.html"

    def get_object(self, queryset=None):
        rayon = get_object_or_404(Rayon, pk=self.kwargs['idRayon'])
        produit = get_object_or_404(Produit, pk=self.kwargs['refProd'])
        return get_object_or_404(Contenir, nomRayon=rayon, nomprod=produit)

    def get_form(self,form_class=None):
        form = super().get_form(form_class)
        form.fields["nomprod"].disabled = True
        return form
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        contenir = form.save(commit=False)
        contenir.nomRayon = get_object_or_404(Rayon, pk=self.kwargs['idRayon'])
        contenir.nomprod = get_object_or_404(Produit, pk=self.kwargs['refProd'])

        if contenir.qte is None or contenir.qte <= 0:
            Contenir.objects.filter(pk=self.get_object().pk).delete()
            return redirect('dtl_rayon', pk=contenir.nomRayon.pk)

        contenir.save()
        return redirect('dtl_rayon', pk=contenir.nomRayon.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ray'] = get_object_or_404(Rayon, pk=self.kwargs['idRayon'])
        context['prod'] = get_object_or_404(Produit, pk=self.kwargs['refProd'])
        context['titremenu'] = "Modifier la quantité"
        return context
class ContenirDeleteView(DeleteView):
    model = Contenir
    template_name = "monApp/delete_contenir.html"

    def get_object(self, queryset=None):
        rayon = get_object_or_404(Rayon, pk=self.kwargs['idRayon'])
        produit = get_object_or_404(Produit, pk=self.kwargs['refProd'])
        return get_object_or_404(Contenir, nomRayon=rayon, nomprod=produit)

    def post(self, request, *args, **kwargs):
        contenir = self.get_object()
        rayon_id = contenir.nomRayon.pk
        contenir.delete()
        return redirect('dtl_rayon', pk=rayon_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ray'] = get_object_or_404(Rayon, pk=self.kwargs['idRayon'])
        context['prod'] = get_object_or_404(Produit, pk=self.kwargs['refProd'])
        context['titremenu'] = "Supprimer le produit du rayon"
        return context