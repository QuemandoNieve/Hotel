from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['mascota', 'fecha_inicio', 'fecha_fin']

