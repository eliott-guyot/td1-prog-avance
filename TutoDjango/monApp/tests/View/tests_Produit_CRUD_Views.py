from datetime import date
from django.urls import reverse
from django.test import TestCase
from monApp.models import Produit
from django.contrib.auth.models import User


class ProduitCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_Produit_create_view_get(self):
        response = self.client.get(reverse('crt-prdt'))  # Utilisation du nom de l'URL
        self.assertEqual(response.status_code, 200)
        # Adapter au nom réel du template (minuscules)
        self.assertTemplateUsed(response, 'monApp/create_produit.html')

    def test_Produit_create_view_post_valid(self):
        data = {
           "intituleProd": "ProduitPourTestCreation",
           "prixUnitaireProd": "1.23",
           "dateDeFabrication": date.today().isoformat()
        }
        response = self.client.post(reverse('crt-prdt'), data)
        # si la vue renvoie 200 => formulaire invalide, afficher erreurs pour debug
        if response.status_code != 302:
            form = response.context.get('form')
            errors = form.errors if form is not None else 'no form in context'
            self.fail(f"Creation POST did not redirect; status={response.status_code}; form errors: {errors}")
        # Vérifie qu'un objet a été créé
        self.assertEqual(Produit.objects.count(), 1)
        self.assertEqual(Produit.objects.last().intituleProd, 'ProduitPourTestCreation')


class ProduitDetailViewTest(TestCase):
    def setUp(self):
        self.ctgr = Produit.objects.create(intituleProd="ProduitPourTestDetail", prixUnitaireProd="1.23")

    def test_Produit_detail_view(self):
        response = self.client.get(reverse('dtl_prdt', args=[self.ctgr.refProd]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/detail_produit.html')
        self.assertContains(response, 'ProduitPourTestDetail')


class ProduitUpdateViewTest(TestCase):
    def setUp(self):
        self.ctgr = Produit.objects.create(intituleProd="ProduitPourTestUpdate", prixUnitaireProd="1.23")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_Produit_update_view_get(self):
        response = self.client.get(reverse('prdt-chng', args=[self.ctgr.refProd]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/update_produit.html')

    def test_update_view_post_valid(self):
        self.assertEqual(self.ctgr.intituleProd, 'ProduitPourTestUpdate')
        data = {
                'intituleProd': 'ProduitPourTestAfterUpdate',
                'prixUnitaireProd': '2.34',
                'dateDeFabrication': date.today().isoformat()
            }        
        response = self.client.post(reverse('prdt-chng', args=[self.ctgr.refProd]), data)
        if response.status_code != 302:
            form = response.context.get('form')
            errors = form.errors if form is not None else 'no form in context'
            self.fail(f"Update POST did not redirect; status={response.status_code}; form errors: {errors}")
        # Recharger l'objet depuis la base de données
        self.ctgr.refresh_from_db()
        self.assertEqual(self.ctgr.intituleProd, 'ProduitPourTestAfterUpdate')


class ProduitDeleteViewTest(TestCase):
    def setUp(self):
        self.ctgr = Produit.objects.create(intituleProd="ProduitPourTesDelete", prixUnitaireProd="1.23")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_Produit_delete_view_get(self):
        response = self.client.get(reverse('dlt-prdt', args=[self.ctgr.refProd]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/delete_produit.html')

    def test_Produit_delete_view_post(self):
        response = self.client.post(reverse('dlt-prdt', args=[self.ctgr.refProd]))
        # Vérifier la redirection après la suppression
        self.assertEqual(response.status_code, 302)
        # Vérifier que l'objet a été supprimé
        self.assertFalse(Produit.objects.filter(refProd=self.ctgr.refProd).exists())
        # Vérifier que la redirection est vers la liste des produits
        self.assertRedirects(response, reverse('lst_prdts'))