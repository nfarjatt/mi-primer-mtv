from django.urls import URLPattern
from familia import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("agregar/", views.agregar, name="agregar"),
    path("borrar/<identificador>", views.borrar, name="borrar") 
]  