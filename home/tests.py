from django.test import TestCase

from .Seguridad import Seguridad
import unittest
# Create your tests here.

class TestSeguridad(unittest.TestCase):

    def test_correo_valido(self):
        seguridad = Seguridad()
        fail_msg = 'Correo electrónico inválido'
        correos = {
            'anita-lavaba-latinahola@gmail-usb.ve': '',
            'anita-lavaba- latinahola@gmail-usb.ve': fail_msg,
            'correo@coreeo': fail_msg,
            'coreo@coreeo.com': '',
            'correo@correo.com.com': '',
            '    @correo.com': fail_msg
        }
        for key in correos:
            self.assertEqual(seguridad.correo_valido(key), correos[key])

    def test_password_valido(self):
        # longitud entre 8 y 16 caracteres
        # No carcteres especiales
        # Al menos 3 letras y almenos una de ellas debe ser mayuscula
        # contener al menos un digito
        fail_msg = 'Clave inválida'
        seguridad = Seguridad()
        passwords = {
            'a'*7: fail_msg, # muy corta
            'a'*17: fail_msg, # muy larga
            'a'*18: fail_msg, # muy larga
            '1a'*5: fail_msg, # Al menos una mayuscula
            'aA'*4: fail_msg, # Al menos un digito
            '$abC123abC': fail_msg, # no caracteres especiales
            '_abC123abC': fail_msg, # no caracteres especiales
            '$abC123abC': fail_msg, # no caracteres especiales
            'PasswordCo123': '',
        }
        for key in passwords:
            self.assertEqual(seguridad.clave_valida(key), passwords['key'])
