from django.contrib.auth.models import User as djangoUser


class Relatorio:
    def __init__(
            self,
            membro=None,
            conteudo=None,
            curso=None,
            naula=None,
            checkin=None,
            checkout=None
    ):
        self.membro = membro
        self.conteudo = conteudo
        self.curso = curso
        self.naula = naula
        self.checkin = checkin
        self.checkout = checkout

    @staticmethod
    def from_json(dados):
        return Relatorio(
            membro=dados['membro'],
            conteudo=dados['conteudo'],
            curso=dados['curso'],
            naula=dados['naula'],
            checkin=dados['checkin'],
            checkout=dados['checkout']
        )

    def to_json(self):
        return {
            'membro': self.membro,
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
            situacao=None,
            pwd=None,
            hrs_semana=None,
            email=None
    ):
        self.username = username
        self.last_login = last_login
        self.situacao = situacao
        self._pwd = pwd
        self.hrs_semana = hrs_semana
        self.email = email if email else "null@null.com"

    @staticmethod
    def from_json(dados):
        return Usuario(
            username=dados['username'],
            last_login=dados['last_login'],
            situacao=dados['situacao'],
            hrs_semana=dados['hrs_semana']
        )

    def to_json(self):
        return {
            'username': self.username,
            'last_login': self.last_login,
            'situacao': self.situacao,
            'hrs_semana': self.hrs_semana
        }

    def create_and_save(self):
        djangoUser.objects.create_user(self.nome, self.email, self._pwd)


# to add a user
# Usuario(nome="slim", pwd="123").create_and_save()
# print("Usuario adicionado!")
