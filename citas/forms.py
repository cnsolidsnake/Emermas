from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario, Cita

# Formulario de registro de usuario
class RegistroForm(UserCreationForm):
    correo = forms.EmailField(required=True, label='Correo Electrónico')

    class Meta:
        model = Usuario
        fields = ['username', 'correo', 'password1', 'password2']

# Formulario de ingreso de usuario
class IngresoForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario")

# Formulario para solicitar citas
class SolicitarCitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['especialidad', 'fecha', 'hora']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

# Formulario para cancelar citas
class CancelarCitaForm(forms.Form):
    cita_id = forms.IntegerField(widget=forms.HiddenInput())
