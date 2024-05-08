from django.urls import include, path

from . import views

from maestro.views import *
app_name = "maestro"

urlpatterns = [ 
    path("DetalleMaestro/<int:idMaestro>", DetalleMaestro),  
    path("nuevoMaestro", nuevoMaestro),
    path("EditarMaestro/<int:id>", EditarMaestro),   
    path("EliminarMaestro/<int:id>", EliminarMaestro),
    
]