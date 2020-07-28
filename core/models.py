class Relatorio:
    def __init__(
            self,
            membro=None,
            data=None,
            conteudo=None
    ):
        self.membro = membro
        self.data = data
        self.conteudo = conteudo

    @staticmethod
    def from_json(dados):
        return Relatorio(
            membro=dados['membro'],
            data=dados['data'],
            conteudo=dados['conteudo']
        )

    def to_json(self):
        return {
            'membro': self.membro,
            'data': self.data,
            'conteudo': self.data
        }


# class Membro:
#     def __init__(
#             self,
#             nome=None,
#     ):
#         self.nome = nome
#
#     @staticmethod
#     def from_json(dados):
#         return Membro(
#             nome=dados['nome']
#         )
#
#     def to_json(self):
#         return {
#             'nome': self.nome
#         }
