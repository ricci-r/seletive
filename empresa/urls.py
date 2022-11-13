
from django.urls import path

from empresa import views

urlpatterns = [
    path("add/", views.nova_empresa, name="nova_empresa"),
    path('list/', views.empresas, name="empresas"),
    path('delete/<int:id>', views.excluir_empresa, name="excluir_empresa"),
    path('edit/<int:id>', views.empresa, name="empresa_unica"),
]
