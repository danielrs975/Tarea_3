import re

# Implementacion de la clase Seguridad que se va a encargar
# de la creacion de usuarios del sistema.
class Seguridad():

    def __init__(self):
        self.usuariosRegistrados = {}

    # Metodo para registrar un usuario
    def registrarUsuario(self, correo, clave, repetirClave):
        # Analizar si el correo tiene el formato correcto
        if not self.correo_valido(correo):
            return 'Correo electrónico inválido'

        # Analizar tiene el formato correcto
        if not self.clave_valida(clave):
            return 'Clave inválida'

        # Ve si las clave y la confirmacion de la clave son iguales
        if clave != repetirClave:
            return 'Claves distintas'

        # Si pasa las verificaciones anteriores se agrega al diccionario
        self.usuariosRegistrados[correo] = clave
        return ''

    # Metodo para ingresar al sistema
    def ingresarUsuario(self, correo, clave):
        # Verificar que el correo existe en el diccionario
        if not (correo in self.usuariosRegistrados):
            return 'Usuario inválido'

        # Verificar que la clave corresponda con el correo 
        if self.usuariosRegistrados[correo] != clave:
            return 'Clave inválida'

        return 'Usuario aceptado'


    def correo_valido(self, correo):
        # Se realiza a traves de expresiones regulares
        patron = re.compile('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$')

        if patron.match(correo) == None:
            return False
        else:
            return True

    def clave_valida(self, clave):

        # Primer requerimiento. Longitud de la clave entre 8 y 16 caracteres
        if len(clave) < 8 and len(clave) > 16:
            return False

        # Debe contener al menos tres letras y al menos una de ellas debe ser mayusculas y una
        # miniscula

        contadorMayuscula = 0
        contadorMiniscula = 0
        contadorDigitos = 0

        # No debe incluir caracteres especiales
        for i in clave:
            if self.esMayuscula(i):
                contadorMayuscula = contadorMayuscula + 1
            elif self.esMinuscula(i):
                contadorMiniscula = contadorMiniscula + 1
            elif self.esDigito(i):
                contadorDigitos = contadorDigitos + 1
            elif self.esUnCaracterEspecial(i):
                return False

        if len(clave) < 3:
            return False

        if contadorMayuscula == 0 or contadorMiniscula == 0:
            return False

        if contadorDigitos == 0:
            return False

        return True

    # Funciones de soporte

    def esUnCaracterEspecial(self, i):
        return (ord(i) < 65 or ord(i) > 90) and (ord(i) < 97 or ord(i) > 122) and (ord(i) < 48 or ord(i) > 57)

    def esMayuscula(self, i):
        return ord(i) >= 65 and ord(i) <= 90

    def esMinuscula(self, i):
        return ord(i) >= 97 and ord(i) <= 122

    def esDigito(self, i):
        return ord(i) >= 48 and ord(i) <= 57