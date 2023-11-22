from django import forms

STATUS_OP = [
    ("1", "Activo"),
    ("0", "Baja"),
]

class CrearCarrera(forms.Form):
    nombre1 = forms.CharField(label="Nombre:",max_length=80,required=True)
    status1 = forms.ChoiceField(choices=STATUS_OP)
