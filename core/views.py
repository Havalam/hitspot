from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from datetime import datetime as dt

from .models import Relatorio, Usuario
from hitspot.db import getdb


db = getdb()


@login_required(login_url='/login')
def index(request):
    if str(request.method) == "POST":
        user = str(request.user)
        relatorio = Relatorio(
            membro=user,
            checkout=get_time(),
            checkin=get_last_user_checkin(user),
            conteudo=request.POST["conteudo"],
            naula=request.POST["naula"],
            curso=request.POST["curso"]
        )
        db["relatorios"].insert_one(relatorio.to_json())
        logout(request)
        return redirect("login")
    return render(request, "index.html")


def logar_usuario(request):
    erro = False
    if str(request.method) == 'POST':
        print(request.POST)
        username = request.POST['username']
        pwd = request.POST['pwd']
        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
            db["checkins"].insert_one({
                "username": username,
                "checkin": get_time()
            })
            return redirect('index')
        erro = True
    context = {"erro": erro}
    return render(request, "login.html", context)


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


def get_time():
    date_format = "%Y-%m-%dT%H:%M:%S.000Z"
    return dt.strptime(dt.now().strftime(date_format), date_format)


def get_last_user_checkin(user):
    checkins = list()
    data = db["checkins"].find({'username': user})
    for checkin in data: checkins.append(checkin)
    return checkins[-1]["checkin"]
