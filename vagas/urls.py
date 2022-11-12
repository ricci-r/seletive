from django.urls import path

from vagas import views

urlpatterns = [
    path('nova-vaga/', views.nova_vaga, name="nova_vaga"),
    path('vaga/<int:id>', views.vaga, name="vaga"),
    path('nova-tarefa/<int:id_vaga>', views.nova_tarefa, name="nova_tarefa"),
    path('realizar-tarefa/<int:id>', views.realizar_tarefa, name="realizar_tarefa"),
]
