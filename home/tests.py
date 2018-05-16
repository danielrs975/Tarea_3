from django.test import TestCase

from .Seguridad import Seguridad
import unittest
# Create your tests here.

class TestSeguridad(unittest.TestCase):

    def test_correo_valido(self):
        seguridad = Seguridad()
        correos = {
            'anita-lavaba-latinahola@gmail-usb.ve': True,
            'anita-lavaba- latinahola@gmail-usb.ve': False,
            'correo@coreeo': False,
            'coreo@coreeo.com': True,
            'correo@correo.com.com': True,
            '    @correo.com': False
        }
        for key in correos:
            self.assertEqual(seguridad.correo_valido(key), correos[key])

    def test_password_valido(self):
        # longitud entre 8 y 16 caracteres
        # No carcteres especiales
        # Al menos 3 letras y almenos una de ellas debe ser mayuscula
        # contener al menos un digito
        seguridad = Seguridad()
        passwords = {
            'a'*7: False, # muy corta
            'a'*17: False, # muy larga
            'a'*18: False, # muy larga
            '1a'*5: False, # Al menos una mayuscula
            'aA'*4: False, # Al menos un digito
            '$abC123abC': False, # no caracteres especiales
            '_abC123abC': False, # no caracteres especiales
            '$abC123abC': False, # no caracteres especiales
            'PasswordCo123': True,
        }
        for key in passwords:
            self.assertEqual(seguridad.clave_valida(key), passwords['key'])
