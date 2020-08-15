from django.urls import path
from .views import index, logar_usuario, deslogar_usuario, area_membros, relatorios_membro

urlpatterns = [
    path("", index, name="index"),
    path("login", logar_usuario, name="login"),
    path("logout", deslogar_usuario, name="logout"),
    path("area_membros", area_membros, name="area_membros"),
    path("relatorios_membro/<str:pk>", relatorios_membro, name="relatorios_membro")
]
