from django.test import TestCase
from monApp.models import Rayon
import unittest


class RayonModelTest(TestCase):
    def setUp(self):
        # Créer un attribut Rayon à utiliser dans les tests
        self.ctgr = Rayon.objects.create(nomRayon="RayonPourTest")
    def test_Rayon_creation(self):
        self.assertEqual(self.ctgr.nomRayon, "RayonPourTest")
    def test_string_representation(self):
        self.assertEqual(str(self.ctgr), "RayonPourTest")
    def test_Rayon_updating(self):
        self.ctgr.nomRayon = "RayonPourTests"
        self.ctgr.save()
        # Récupérer l'objet mis à jour
        updated_ctgr = Rayon.objects.get(idRayon=self.ctgr.idRayon)
        self.assertEqual(updated_ctgr.nomRayon, "RayonPourTests")
    def test_Rayon_deletion(self):
        self.ctgr.delete()
        self.assertEqual(Rayon.objects.count(), 0)