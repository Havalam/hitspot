from django.contrib.auth.models import User as djangoUser


class Relatorio:
    def __init__(
            self,
            username=None,
            conteudo=None,
            curso=None,
            naula=None,
            checkin=None,
            checkout=None
    ):
        self.username = username
        self.conteudo = conteudo
        self.curso = curso
        self.naula = naula
        self.checkin = checkin
        self.checkout = checkout

    @staticmethod
    def from_json(dados):
        return Relatorio(
            username=dados['username'],
            conteudo=dados['conteudo'],
            curso=dados['curso'],
            naula=dados['naula'],
            checkin=dados['checkin'],
            checkout=dados['checkout']
        )

    def to_json(self):
        return {
            'username': self.username,
            'conteudo': self.conteudo,
            'curso': self.curso,
            'naula': self.naula,
            'checkin': self.checkin,
            'checkout': self.checkout
        }


class Usuario:
    def __init__(
            self,
            username=None,
            last_login=None,
            pwd=None,
            hrs_semana=None,
            email=None,
            relatorios=None
    ):
        self.username = username
        self.last_login = last_login
        self._pwd = pwd
        self.hrs_semana = hrs_semana
        self.email = email if email else "null@null.com"
        self.relatorios = relatorios

    @staticmethod
    def from_json(dados):
        return Usuario(
            username=dados['username'],
            last_login=dados['last_login'],
            hrs_semana=dados['hrs_semana']
        )

    @staticmethod
    def from_djangoUser(user):
        return Usuario(
            username=user.username,
            last_login=user.last_login,
        )

    def to_json(self):
        return {
            'username': self.username,
            'last_login': self.last_login,
            'hrs_semana': self.hrs_semana
        }

    def create_and_save(self):
        djangoUser.objects.create_user(self.username, self.email, self._pwd)

    @staticmethod
    def get_all():
        return djangoUser.objects.all()


# to add a user
# Usuario(username="danielb", pwd="123").create_and_save()
# print("Usuario adicionado!")
