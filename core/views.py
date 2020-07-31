from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from datetime import datetime as dt, timedelta as delta

from .models import Relatorio, Usuario
from hitspot.db import getdb


db = getdb()


@login_required(login_url='/login')
def index(request):
    if str(request.method) == "POST":
        user = str(request.user)
        relatorio = Relatorio(
            username=user,
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


def area_membros(request):
    usuarios = list()
    for u in Usuario().get_all():
        aux_user = Usuario.from_djangoUser(u)
        aux_user.hrs_semana, aux_user.relatorios = get_hours_week_and_reports_user(u.username)
        usuarios.append(aux_user)
    context = {
        "usuarios": usuarios
    }
    return render(request, "area_membros.html", context)


def relatorios_membro(request, pk):
    null, relatorios = get_hours_week_and_reports_user(pk)
    context = {
        "username": pk,
        "relatorios": relatorios
    }
    return render(request, "relatorios_membro.html", context)


def logar_usuario(request):
    erro = False
    if str(request.method) == 'POST':
        username = request.POST['username']
        pwd = request.POST['pwd']
        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('index')
        erro = True
    context = {"erro": erro}
    return render(request, "login.html", context)


def get_time():
    date_format = "%Y-%m-%d %H:%M:%S.000Z"
    return dt.strptime(dt.now().strftime(date_format), date_format)


def get_last_user_checkin(user):
    usuarios = Usuario().get_all()
    for u in usuarios:
        if u.username == user:
            return u.last_login


def get_hours_week_and_reports_user(user):
    segundos = 0
    relatorios = list()
    data = db["relatorios"].find({'username': user})
    hj = dt.now()
    segunda = hj - delta(days=hj.weekday())
    for r in data:
        if r["checkin"] > segunda:
            segundos += (r["checkout"] - r["checkin"]).total_seconds()
        relatorios.append(Relatorio.from_json(r))
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    return f"{horas} horas e {minutos} minutos", relatorios
