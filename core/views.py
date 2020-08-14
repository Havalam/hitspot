from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from datetime import datetime as dt, timedelta as delta, timezone

from .models import Relatorio, Usuario
from hitspot.db import getdb


db = getdb()


@login_required(login_url='/login')
def index(request):
    user = str(request.user)
    checkin = get_last_user_checkin(user)
    if str(request.method) == "POST":
        relatorio = Relatorio(
            username=user,
            checkout=get_time(),
            checkin=checkin,
            conteudo=request.POST["conteudo"],
            naula=request.POST["naula"],
            curso=request.POST["curso"]
        )
        db["relatorios"].insert_one(relatorio.to_json())
        logout(request)
        return redirect("login")
    content = {
        'checkin': get_millis_since_epoch(checkin)
    }
    return render(request, "index.html", content)


def area_membros(request):
    usuarios = list()
    for u in Usuario().get_all():
        aux_user = Usuario.from_djangoUser(u)
        aux_user.hrs_semana, aux_user.relatorios = get_hours_week_and_reports_user(u.username)
        if aux_user.last_login is not None:
            aux_user.last_login += get_delta_less3()
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
    return dt.strptime(dt.now(get_sp_tz()).strftime(date_format), date_format)


def get_last_user_checkin(user):
    usuarios = Usuario().get_all()
    for u in usuarios:
        if u.username == user:
            u.last_login += get_delta_less3()
            return u.last_login


def get_delta_less3():
    return delta(hours=-3)


def get_sp_tz():
    return timezone(get_delta_less3())


def get_hours_week_and_reports_user(user):
    segundos = 0
    relatorios = list()
    data = db["relatorios"].find({'username': user})
    hj = dt.now(get_sp_tz())
    if hj.weekday():
        d = delta(days=hj.weekday())
        s = hj - d
    else:
        s = hj
    segunda = dt(s.year, s.month, s.day)
    for r in data:
        if r["checkin"] > segunda:
            segundos += (r["checkout"] - r["checkin"]).total_seconds()
        relatorios.append(Relatorio.from_json(r))
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    return f"{horas} horas e {minutos} minutos", relatorios


def get_millis_since_epoch(h):
    indate = dt(h.year, h.month, h.day, h.hour, h.minute)
    epoch = dt.utcfromtimestamp(0) + get_delta_less3()
    return (indate - epoch).total_seconds() * 1000.0
