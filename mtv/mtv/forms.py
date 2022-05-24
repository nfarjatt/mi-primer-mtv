from django import forms

class PersonaForm(forms, form):
    nombre = forms.CharField(label="Nombre")
    apellido = forms.CharField(label="Apellido")
    email =  forms.CharField(label="Email")
    fecha_nacimiento = forms.DataField(label="fecha:nacimiento", input_formats=["%d/%m/%Y"]),
    widget=forms.TextInput(attrs={"placeholder" : 30/12/1995})