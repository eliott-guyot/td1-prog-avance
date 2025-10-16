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
        self.assertEqual(self.ctgr.qte, 2)
    def test_string_representation(self):
        expected = (self.prdt, self.ray, self.ctgr.qte)
        self.assertEqual(self.ctgr.__str__(), expected)
    def test_Contenir_updating(self):
        self.ctgr.qte = 2
        self.ctgr.save()
        # Récupérer l'objet mis à jour
        updated_ctgr = Contenir.objects.get(pk=self.ctgr.pk)
        self.assertEqual(updated_ctgr.qte, 2)
    def test_Contenir_deletion(self):
        self.ctgr.delete()
        self.assertEqual(Contenir.objects.count(), 0)