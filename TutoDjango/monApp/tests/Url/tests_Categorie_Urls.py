from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from monApp.models import Categorie
from monApp.views import CategorieCreateView, CategorieDeleteView, CategorieListView, CategorieDetailView, CategorieUpdateView
class CategorieUrlsTest(TestCase):
    def test_categorie_list_url_is_resolved(self):
        url = reverse('lst_cat')
        self.assertEqual(resolve(url).view_name, 'lst_cat')
        self.assertEqual(resolve(url).func.view_class,CategorieListView)
    def test_categorie_detail_url_is_resolved(self):
        url = reverse('dtl_cat', args=[1])
        self.assertEqual(resolve(url).view_name, 'dtl_cat')
        self.assertEqual(resolve(url).func.view_class, CategorieDetailView)
    def test_categorie_create_url_is_resolved(self):
        url = reverse('crt-cat')
        self.assertEqual(resolve(url).view_name, 'crt-cat')
        self.assertEqual(resolve(url).func.view_class, CategorieCreateView)
    def test_categorie_update_url_is_resolved(self):
        url = reverse('cat-chng', args=[1])
        self.assertEqual(resolve(url).view_name, 'cat-chng')
        self.assertEqual(resolve(url).func.view_class, CategorieUpdateView)
    def test_categorie_delete_url_is_resolved(self):
        url = reverse('dlt-cat', args=[1])
        self.assertEqual(resolve(url).view_name, 'dlt-cat')
        self.assertEqual(resolve(url).func.view_class, CategorieDeleteView)
    def test_categorie_list_response_code(self):
        response = self.client.get(reverse('lst_cat'))
        self.assertEqual(response.status_code, 200)
    def setUp(self):
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTest")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
    def test_categorie_detail_response_code(self):
        url = reverse('dtl_cat', args=[self.ctgr.idCat]) #idCat existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_categorie_detail_response_code_KO(self):
        url = reverse('dtl_cat', args=[9999]) # idCat non existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    def test_categorie_create_response_code_OK(self):
        response = self.client.get(reverse('crt-cat'))
        self.assertEqual(response.status_code, 200)
    def test_categorie_update_response_code_OK(self):
        url = reverse('cat-chng', args=[self.ctgr.idCat]) # idCat existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_categorie_update_response_code_KO(self):
        url = reverse('cat-chng', args=[9999]) # idCat non existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    def test_categorie_delete_response_code_OK(self):
        url = reverse('dtl_cat', args=[self.ctgr.idCat]) # idCat existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_categorie_delete_response_code_KO(self):
        url = reverse('dtl_cat', args=[9999]) # idCat non existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    def test_redirect_after_categorie_creation(self):
        response = self.client.post(reverse('crt-cat'), {'nomCat': 'CategoriePourTestRedirectionCreation'} )
        # Statut 302 = redirection
        self.assertEqual(response.status_code, 302)
        # Redirection vers la vue de detail
        self.assertRedirects(response, '/monApp/Categorie/2/')
    def test_redirect_after_categorie_updating(self):
        response = self.client.post(reverse('cat-chng', args=[self.ctgr.idCat]),
        data={"nomCat": "CategoriePourTestRedirectionMaj"})
        # Statut 302 = redirection
        self.assertEqual(response.status_code, 302)
        # Redirection vers la vue de detail
        self.assertRedirects(response, f'/monApp/categorie/{self.ctgr.idCat}/update/')
    def test_redirect_after_categorie_deletion(self):
        response = self.client.post(reverse('dlt-cat', args=[self.ctgr.pk]))
        # Vérifie qu'on a bien une redirection
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lst_cat'))
        # Vérifie que la catégorie a bien été supprimée de la base
        self.assertFalse(Categorie.objects.filter(pk=self.ctgr.pk).exists())