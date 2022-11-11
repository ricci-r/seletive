
from django.urls import path

from empresa import views

urlpatterns = [
    path("nova-empresa/", views.nova_empresa, name="nova_empresa"),
    path('empresas/', views.empresas, name="empresas"),
    path('excluir-empresa/<int:id>', views.excluir_empresa, name="excluir_empresa"),
    path('empresa/<int:id>', views.empresa, name="empresa_unica"),
]
