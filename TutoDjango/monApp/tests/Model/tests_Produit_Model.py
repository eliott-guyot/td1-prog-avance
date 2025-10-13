from django.test import TestCase
from monApp.models import Produit
import unittest


class ProduitModelTest(TestCase):
    def setUp(self):
        # Créer un attribut produit à utiliser dans les tests
        self.ctgr = Produit.objects.create(intituleProd="ProduitPourTest", prixUnitaireProd="1.23")
    def test_Produit_creation(self):
        self.assertEqual(self.ctgr.intituleProd, "ProduitPourTest")
    def test_string_representation(self):
        self.assertEqual(str(self.ctgr), "ProduitPourTest")
    def test_Produit_updating(self):
        self.ctgr.intituleProd = "ProduitPourTests"
        self.ctgr.save()
        # Récupérer l'objet mis à jour
        updated_ctgr = Produit.objects.get(refProd=self.ctgr.refProd)
        self.assertEqual(updated_ctgr.intituleProd, "ProduitPourTests")
    def test_Produit_deletion(self):
        self.ctgr.delete()
        self.assertEqual(Produit.objects.count(), 0)