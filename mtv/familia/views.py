from urllib import request
from django.http import HttpResponse
from django import forms

# Create your views here.

def agregar(request):
    if request.method == "POST":
        form = PersonaFrom(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["nombre"]
            email = form.cleaned_data["nombre"]
            fecha_nacimiento = form.cleaned_data["nombre"]
            Persona(nombre=nombre, apellido=apellido, email=email, fecha_nacimiento=fecha_nacimiento,)

            return HttpResponse("/familia/")
    elif request.method == "GET":
        form = PersonaForm()
    else:
        return HttpResponse("Error no conozco ese metodo para ")

    return render(request, "familia/form_carga.html", {"form" : form})


def index(request):
    template = loader.get_template("familia/index.html")
    context = {
        "personas": personas,
    }
    return HttpResponse(template.render(context, request))

