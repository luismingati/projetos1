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
    def __init__(self, imagem,  nome, nota, descricao, duracaoAtividade, tags, servicos, localizacao, comentario):
        self.imagem = imagem
        self.nome = nome
        self.nota = nota
        self.descricao = descricao
        self.duracaoAtividade = duracaoAtividade
        self.tags = tags
        self.servicos = servicos
        self.localizacao = localizacao
        self.comentario = comentario

# atividade1 = Atividade("imagemx", "Praia de bv", 5, "descricao praia bv", 10, ["praia", "cerveja", "drinks"], ["barraquinha"], "rua", ["muuto top", "meio paia"])
# atividade2 = Atividade("imagemx", "Praia de piedade", 5, "descricao praia bv", 10, ["praia", "cerveja", "drinks"], ["barraquinha"], "rua", ["muuto top", "meio paia"])
# atividade3 = Atividade("imagemx", "Praia de pina", 5, "descricao praia bv", 10, ["praia", "cerveja", "drinks"], ["barraquinha"], "rua", ["muuto top", "meio paia"])
#ideia inicial de fazer pesquisa
#def fazerPesquisa()
# praia = []
# praia.append(atividade1)
# praia.append(atividade2)
# praia.append(atividade2)
# for praia in praia:
#     nomePraia = []
    

def main():
    goTo = int(input())

    if goTo == 1:
        #verPerfil()
        pass
    if goTo == 2:
        #verRoteiros()
        pass
    if goTo == 3:
        #verPraias()
        pass
    if goTo == 4:
        #verPasseios()
        pass
    if goTo == 5:
        #verRestaurantes()
        pass
    if goTo == 6:
        #mehoresRoteiros()
        pass
    if goTo == 7:
        #roteirosMaisAvaliados()
        pass
    if goTo == 8:
        #fazerPesquisa()
        pass

def fazLogin(usuario):
    pass

def filtraAtividade(listaAtividades, tags):
    pass

# def verPerfil():
#     if login == True:
#         print(conta)
#     else:
#         print("voce tem login?")
#         if login == True:
#             print("digite seu email e senha")
#         else:
#             print("Cadastre-se")

# def verPraias():
# def verPasseios():
# def verRestaurantes():
#     #obs tem o filtro tambem. ##filtraAtividade(listaAtividades, tags):##
#     for praia in praias:
#         print(f"{praia.nome} --- digite [{index}]")
#     print("qual praia voce quer ver?")
#     print("Quer curtir alguma praia?")
#     print("quer ver os filtros?") 

# def verPraia():
#     print(praiaTal)
#     #obs: so pode fazer isso quyando logado == True
#         print("voce quer adicionar ela ao seu roteiro?")
#         print("voce quer cutir essa praia?")
#         print("voce quer fazer um comentario?")

def filtrar(praias[]):
    print("quer filtrar por isso?")
    print("quer filtrar por aquilo?")
