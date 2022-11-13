
from django.urls import path

from empresa import views

urlpatterns = [
    path("", views.home, name="home"),
    path('list/', views.empresas, name="empresas"),
    path("add/", views.nova_empresa, name="nova_empresa"),
    path('delete/<int:id>', views.excluir_empresa, name="excluir_empresa"),
    path('edit/<int:id>', views.empresa, name="empresa_unica"),
]
