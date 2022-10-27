class Usuario:
    def __init__(self, nome, email, senha, repeteSenha, curtidas, roteiros):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.repeteSenha = repeteSenha
        self.curtidas = curtidas
        self.roteiros = roteiros  

    def fazComentario(self, atividade, texto, nota, imagem):
        pass
    
    def curtir(self, atividade):
        pass

    def adicionarRoteiro(self, atividade):
        pass
    
    


class Atividade:
    def __init__(self, imagem,  nome, nota, descricao,
                 duracaoAtividade, tags, servicos, localizacao, avaliacao):
        self.imagem = imagem
        self.nome = nome
        self.nota = nota
        self.descricao = descricao
        self.duracaoAtividade = duracaoAtividade
        self.tags = tags
        self.servicos = servicos
        self.localizacao = localizacao
        self.avaliacao = avaliacao



def fazLogin(usuario):
    pass

def filtraAtividade(listaAtividades, tags):
    pass


