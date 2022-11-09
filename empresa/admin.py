from django.contrib import admin

from empresa.models import Empresa, Tecnologias, Vagas

admin.site.register(Tecnologias)
admin.site.register(Empresa)
admin.site.register(Vagas)

# Register your models here.
