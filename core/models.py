class Relatorio:
    def __init__(
            self,
            membro=None,
            data=None,
            conteudo=None,
            curso=None,
            naula=None,
            checkin=None,
            checkout=None
    ):
        self.membro = membro
        self.data = data
        self.conteudo = conteudo
        self.curso = curso
        self.naula = naula
        self.checkin = checkin
        self.checkout = checkout

    @staticmethod
    def from_json(dados):
        return Relatorio(
            membro=dados['membro'],
            data=dados['data'],
            conteudo=dados['conteudo'],
            curso=dados['curso'],
            naula=dados['naula'],
            checkin=dados['checkin'],
            checkout=dados['checkout']
        )

    def to_json(self):
        return {
            'membro': self.membro,
            'data': self.data,
            'conteudo': self.data,
            'curso': self.curso,
            'naula': self.naula,
            'checkin': self.checkin,
            'checkout': self.checkout
        }


class Usuario:
    def __init__(
            self,
            nome=None,
            last_login=None,
            situacao=None,
            pwd=None,
            hrs_semana=None
    ):
        self.nome = nome
        self.last_login = last_login
        self.situacao = situacao
        self._pwd = pwd
        self.hrs_semana = hrs_semana

    @staticmethod
    def from_json(dados):
        return Usuario(
            nome=dados['nome'],
            last_login=dados['last_login'],
            situacao=dados['situacao'],
            pwd=dados['pwd'],
            hrs_semana=dados['hrs_semana']
        )

    def to_json(self):
        return {
            'nome': self.nome,
            'last_login': self.last_login,
            'situacao': self.situacao,
            'pwd': self._pwd,
            'hrs_semana': self.hrs_semana
        }
