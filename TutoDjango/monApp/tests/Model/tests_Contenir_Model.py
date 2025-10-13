from django.test import TestCase
from monApp.models import Contenir,Produit,Rayon
import unittest


class ContenirModelTest(TestCase):
    def setUp(self):
        # Créer un attribut Contenir à utiliser dans les tests
        self.prdt = Produit.objects.create(intituleProd="ProduitPourTest", prixUnitaireProd="1.23")
        self.ray = Rayon.objects.create(nomRayon="RayonPourTest")
        self.ctgr = Contenir.objects.create(qte=2, nomprod=self.prdt, nomRayon=self.ray)
    def test_Contenir_creation(self):
        self.assertEqual(self.ctgr.nomContenir, 2,nomprod=self.prdt, nomRayon=self.ray)
    def test_string_representation(self):
        self.assertEqual(str(self.ctgr),self.prdt,self.ray,self.ctgr.qte )
    def test_Contenir_updating(self):
        self.ctgr.qte = 2
        self.ctgr.save()
        # Récupérer l'objet mis à jour
        updated_ctgr = Contenir.objects.get(idContenir=self.ctgr.idContenir)
        self.assertEqual(updated_ctgr.qte, 2)
    def test_Contenir_deletion(self):
        self.ctgr.delete()
        self.assertEqual(Contenir.objects.count(), 0)