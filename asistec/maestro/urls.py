from django.urls import path
from .views import MaestroListView, MaestroCreateView, MaestroUpdateView, MaestroDeleteView

urlpatterns = [
    path('', MaestroListView.as_view(), name='listado_maestros'),
    path('nuevo/', MaestroCreateView.as_view(), name='nuevo_maestro'),
    path('editar/<int:id>/', MaestroUpdateView.as_view(), name='editar_maestro'),
    path('eliminar/<int:id>/', MaestroDeleteView.as_view(), name='eliminar_maestro'),
]
