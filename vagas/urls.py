from django.urls import path

from vagas import views

urlpatterns = [
    path('list/<int:id>', views.vaga, name="vaga"),
    path('add/', views.nova_vaga, name="nova_vaga"),
    path('task/<int:id_vaga>', views.nova_tarefa, name="nova_tarefa"),
    path('perform-task/<int:id>', views.realizar_tarefa, name="realizar_tarefa"),
    path('send-mail/<int:id_vaga>', views.envia_email, name="envia_email"),
]
