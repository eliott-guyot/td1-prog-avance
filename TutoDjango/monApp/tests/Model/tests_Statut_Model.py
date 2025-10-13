from django.test import TestCase
from monApp.models import Statut
import unittest


class StatutModelTest(TestCase):
    def setUp(self):
        # Créer un attribut produit à utiliser dans les tests
        self.stt = Statut.objects.create(libelleStatut="StatutPourTest")
    def test_Statut_creation(self):
        self.assertEqual(self.stt.libelleStatut, "StatutPourTest")
    def test_string_representation(self):
        self.assertEqual(str(self.stt), "StatutPourTest")
    def test_Statut_updating(self):
        self.stt.libelleStatut = "StatutPourTests"
        self.stt.save()
        # Récupérer l'objet mis à jour
        updated_stt = Statut.objects.get(idStatut=self.stt.idStatut)
        self.assertEqual(updated_stt.libelleStatut, "StatutPourTests")
    def test_Statut_deletion(self):
        self.stt.delete()
        self.assertEqual(Statut.objects.count(), 0)