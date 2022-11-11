from django.urls import path

from vagas import views

urlpatterns = [
    path('nova-vaga/', views.nova_vaga, name="nova_vaga"),
    path('vaga/<int:id>', views.vaga, name="vaga"),
]
