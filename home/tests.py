from django.test import TestCase

from Seguridad import Seguridad
import unittest
# Create your tests here.

class TestSeguridad(unittest.TestCase):

    def test_registrar_usuario(self):
        seguridad = Seguridad()
