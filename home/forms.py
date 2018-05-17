from django import forms
from .Seguridad import Seguridad

class RegisterForm(forms.Form):
    email = forms.EmailField(label='Correo electronico')
    clave = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    conf_clave = forms.CharField(widget=forms.PasswordInput, label='Confirmacion contraseña')

    def clean_clave(self):
        seguridad = Seguridad()
        clave = self.cleaned_data['clave']
        if not seguridad.clave_valida(clave):
            raise forms.ValidationError('Clave invalida')
        return clave

    def clean_conf_clave(self):
        seguridad = Seguridad()
        email = self.cleaned_data['email']
        clave = self.cleaned_data['clave']
        clave_conf = self.cleaned_data['conf_clave']
        mensaje = seguridad.registrarUsuario(email, clave, clave_conf)
        if mensaje:
            raise forms.ValidationError(mensaje)

        return clave_conf