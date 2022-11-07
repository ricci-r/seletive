from django.shortcuts import render


def nova_empresa(request):
    return render(request, "nova-empresa.html")