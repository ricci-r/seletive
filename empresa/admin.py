from django.contrib import admin

from empresa.models import Empresa, Tecnologias, Vagas
from vagas.models import Emails, Tarefa

admin.site.register(Tecnologias)
admin.site.register(Empresa)
admin.site.register(Vagas)
admin.site.register(Tarefa)
admin.site.register(Emails)
