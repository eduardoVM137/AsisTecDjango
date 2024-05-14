from django.urls import include, path

from . import views

from maestro.views import *
app_name = "maestro"

urlpatterns = [  
    path("nuevoMaestro", nuevoMaestro),
    path("EditarMaestro/<int:id>", EditarMaestro),   
    path("EliminarMaestro/<int:id>", EliminarMaestro), 
    
]