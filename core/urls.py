from django.urls import path
from .views import index, login, area_membros, relatorios_membro

urlpatterns = [
    path("", index, name="index"),
    path("login", login, name="login"),
    path("area_membros", area_membros, name="area_membros"),
    path("relatorios_membro", relatorios_membro, name="relatorios_membro")
]
