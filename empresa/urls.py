
from django.urls import path

from empresa import views

urlpatterns = [
    path("nova-empresa/", views.nova_empresa, name="nova_empresa")
]
