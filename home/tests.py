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
            self.assertEqual(seguridad.clave_valida(key), passwords[key])

    def test_registrar_usuario(self):
        seguridad = Seguridad()
        correo_invalido = 'Correo electrónico inválido'
        clave_invalida = 'Clave inválida'
        claves_distintas = 'Claves distintas'
        credenciales = {
            'correo@correo.com': ['passBueno123', 'passBueno123', ''],
            'correo@correo': ['passBueno123', 'passBueno123', correo_invalido],
            'correo2@correo.com': ['passPass', 'passPass', clave_invalida],
            'correo3@correo.com': ['passBueno12', 'passBueno123', claves_distintas],
        }

        for correo in credenciales:
            password1, password2, msg = credenciales[correo]
            self.assertEqual(seguridad.registrarUsuario(correo, password1, password2), msg)

        self.assertTrue(len(seguridad.usuariosRegistrados.keys()) == 1)
        self.assertEqual(
            seguridad.registrarUsuario('correo@correo.com', 'passBueno123', 'passBueno123'),
            'Este usuario ya existe'
            )
        self.assertTrue(seguridad.usuariosRegistrados['correo@correo.com'] == '321oneuBssap')


    def test_ingresar_usuario(self):
        seguridad = Seguridad()
        correos_pass = {
            'correo1@correo1.com': ['passPass123', 'passPass123'],
            'correo2@correo1.com': ['passPass123', 'passPass123'],
            'correo3@correo1.com': ['passPass123', 'passPass123']
        }
        for correo in correos_pass:
            pass1, pass2 = correos_pass[correo]
            seguridad.registrarUsuario(correo, pass1, pass2)

        usuario_aceptado = 'Usuario aceptado'
        usuario_invalido = 'Usuario inválido'
        clave_invalida = 'Clave inválida'
        self.assertEqual(seguridad.ingresarUsuario('correo1@correo1.com', 'passPass123'), usuario_aceptado)
        self.assertEqual(seguridad.ingresarUsuario('correo1@correo1.com', 'p'), clave_invalida)
        self.assertEqual(seguridad.ingresarUsuario('correo1@correo2.com', 'passPass12'), usuario_invalido)
        self.assertEqual(seguridad.ingresarUsuario('correo1@correo3.com', 'p'), usuario_invalido)
