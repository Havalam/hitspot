from django.db import models
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from bson.objectid import ObjectId
from django.contrib.auth.models import User, UserManager, update_last_login


class Relatorio:
    def __init__(
            self,
            usernameid=None,
            conteudo=None,
            atividade=None,
            checkin=None,
            checkout=None
    ):
        self.id = ObjectId()
        self.usernameid = usernameid
        self.conteudo = conteudo
        self.atividade = atividade
        self.checkin = checkin
        self.checkout = checkout

    @staticmethod
    def from_json(dados):
        return Relatorio(
            usernameid=dados['usernameid'],
            conteudo=dados['conteudo'],
            atividade=dados['atividade'],
            checkin=dados['checkin'],
            checkout=dados['checkout']
        )

    def to_json(self):
        return {
            'usernameid': self.usernameid,
            'conteudo': self.conteudo,
            'atividade': self.atividade,
            'checkin': self.checkin,
            'checkout': self.checkout
        }


class Usuario(models.Model):
    id = ObjectId()
    username = models.CharField('Name', max_length=30)
    mail = models.EmailField("Email")
    tarefa_ativa = models.CharField('Active Task', max_length=50)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)
    criado = models.DateField('Created', auto_now_add=True)
    _pwd = models.CharField(_('password'), max_length=128)

    hrs_week = 0
    is_super_user = False

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'mail': self.mail,
            'tarefa_ativa': self.tarefa_ativa,
            'last_login': self.last_login,
            'criado': self.criado,
            'hrs_week': self.hrs_week
        }


class Equipe:
    def __init__(
        self,
        id=ObjectId(),
        criado=None,
        usuarios=list(),
        min_por_rel=25,
        is_plus=False
    ):
        self.id = id
        self.criado = criado
        self.usuarios = usuarios
        self.min_por_rel = min_por_rel
        self.is_plus = is_plus
    
    def from_json(self, dados):
        self.id = ["id"]
        self.criado = ["criado"]
        self.usuarios = ["usuarios"]
        self.min_por_rel = ["min_por_rel"]
        self.is_plus = ["is_plus"]

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "criado": self.criado,
            "usuarios": self.usuarios,
            "min_por_rel": self.min_por_rel,
            "is_plus": self.is_plus,
        }
