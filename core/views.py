from django.shortcuts import render


def index(request):
    context = {

    }
    return render(request, "index.html", context)


def login(request):
    return render(request, "login.html")


def area_membros(request):
    usuarios = list()
    usuarios.append(1)
    usuarios.append(1)
    context = {
        "usuarios": usuarios
    }
    return render(request, "area_membros.html", context)


def relatorios_membro(request):
    relatorios = [1, 2, 3]
    context = {
        "relatorios": relatorios
    }
    return render(request, "relatorios_membro.html", context)
