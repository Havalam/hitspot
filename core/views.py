from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Relatorio, Usuario


@login_required(login_url='/login')
def index(request):
    context = {}
    print(request.user)
    return render(request, "index.html", context)


def logar_usuario(request):
    if str(request.method) == 'POST':
        print(request.POST)
        username = request.POST['username']
        pwd = request.POST['pwd']
        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, "login.html")


@login_required(login_url='/login')
def area_membros(request):
    usuarios = [1, 2, 3]
    context = {
        "usuarios": usuarios
    }
    return render(request, "area_membros.html", context)


@login_required(login_url='/login')
def relatorios_membro(request):
    relatorios = [1, 2, 3]
    context = {
        "relatorios": relatorios
    }
    return render(request, "relatorios_membro.html", context)


def deslogar_usuario(request):
    logout(request)
    return redirect('index')

