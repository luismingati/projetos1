from verRestaurantes import *

class Usuario:
    def __init__(self, nome, email, senha, repeteSenha, curtidas, roteiros):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.repeteSenha = repeteSenha
        self.curtidas = curtidas
        self.roteiros = roteiros  

    def fazComentario(self, atividade, texto, nota, imagem):
        return
    
    def curtir(self, atividade):
        if(atividade in self.curtidas):
            print("Atividade já foi adicionada")
        else:
            self.curtidas.append(atividade)
            
    def removeCurtida(self, atividade):
        if atividade in self.curtidas:
            self.curtidas.remove(atividade)

    def adicionarRoteiro(self, atividade):
        return
    
    
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

praia1 = Atividade( "imagem praia1",  "nome praia 1", [5, 4, 3], "Descrição praia 1", "01:30", ["tag1","tag3","tag6","tag9","tag10"], ["servico1 praia1", "servico2 praia1"], "Localizacao praia 1", ["comentário1 praia1","comentário2 praia1","comentário3 praia1"])
praia2 = Atividade( "imagem praia2",  "nome praia 2", [5, 2, 1], "Descrição praia 2", "02:30", ["tag1","tag2","tag3","tag4","tag5"], ["servico1 praia2", "servico2 praia2"], "Localizacao praia 2", ["comentário1 praia2","comentário2 praia2","comentário3 praia2"])
praia3 = Atividade( "imagem praia3",  "nome praia 3", [3, 4, 5], "Descrição praia 3", "00:30", ["tag2","tag4","tag6","tag8","tag10"], ["servico1 praia3", "servico2 praia3"], "Localizacao praia 3", ["comentário1 praia3","comentário2 praia3","comentário3 praia3"])
praia4 = Atividade( "imagem praia4",  "nome praia 4", [1, 2, 3], "Descrição praia 4", "01:00", ["tag1","tag2","tag4","tag5","tag9"], ["servico1 praia4", "servico2 praia4"], "Localizacao praia 4", ["comentário1 praia4","comentário2 praia4","comentário3 praia4"])
praia5 = Atividade( "imagem praia5",  "nome praia 5", [5, 5, 5], "Descrição praia 5", "03:00", ["tag1","tag3","tag5","tag7","tag9"], ["servico1 praia5", "servico2 praia5"], "Localizacao praia 5", ["comentário1 praia5","comentário2 praia5","comentário3 praia5"])
praias = [praia1, praia2, praia3, praia4, praia5]

passeioMaragogi = Atividade( "imagem passeio Maragogi",  "Passeio à maragogi", [5, 4, 3], "Saindo de maceió, ao norte, você visitará piscinas naturais", "9h", ["Bom para crianças","Natureza","Praia","Pet friendly, Bom para idosos"], ["Catamarã", "Apoio no Restaurante pontal do maragogi"], "Pontal do Maragogi, Rodovia AL 101 Norte, Km 130 s/n Burgalhau - Barra Grande, Maragogi - AL, 57799-000, Brazil", ["Passeio com preço justo","Guias divertidos e engraçados","Ótimo serviço prestado"])
passeioMarape = Atividade( "imagem passeio Marapé",  "Passeio às Dunas de Marapé", [5, 4, 3], "Paraíso ecológico formado entre a Praia de Duas Barras e o Rio Jequiá. Além disso, pode também visualizar falésias.", "7h", ["Natureza","Aventura"], ["passeio de buggy", "Barraquinha","Day-use", "Circuito Pau-de-Arara", "Trilha dos Caetés"], "Povoado Barra de Jequia SN Duas Barras - Jequiá da Praia - Litoral Sul de Alagoas - 50 min de Maceió, Jequiá da Praia, Alagoas 57244-000 Brasil", ["Passeio Perfeito com a guia muito alegre!","Não deixe de fazer o passeio de buggy que sobe as falesias, a vista lá de cima é deslumbrante"])
passeioHibiscus = Atividade( "imagem passeio Hibiscus",  "Passeio à ipipoca no Hibiscus beach club", [5, 4, 3], "Ida a praia de IPIOCA pra aproveitar um dia relaxante no beach club.", "3h30", ["Relaxante","Para casais","Bom para crianças","Natureza","Praia"], ["Passeios Náuticos", "Massagem relaxante","Área HIBISQUINHO para crianças","Passeio de lancha, Stand-up paddling e Caiaque"], "Rodovia AL 101 Norte, Bairro Ipioca Residencial Angra de Ipioca, Maceió, Alagoas 57039-705 Brasil", ["Paraíso!","Praia boa, mas experiência ruim.","Ótimo para casais, mas chegue cedo para pegar lugar."])
passeios = [passeioMaragogi, passeioMarape, passeioHibiscus]

restaurante1 = Atividade( "imagem restaurante1",  "nome restaurante 1", [5, 4, 3], "Descrição restaurante 1", "01:30", ["tag1","tag3","tag6","tag9","tag10"], ["servico1 restaurante1", "servico2 restaurante1"], "Localizacao restaurante 1", ["comentário1 restaurante1","comentário2 restaurante1","comentário3 restaurante1"])
restaurante2 = Atividade( "imagem restaurante2",  "nome restaurante 2", [5, 4, 3], "Descrição restaurante 2", "02:15", ["tag1","tag3","tag6","tag9","tag10"], ["servico1 restaurante2", "servico2 restaurante2"], "Localizacao restaurante 2", ["comentário1 restaurante2","comentário2 restaurante2","comentário3 restaurante2"])
restaurante3 = Atividade( "imagem restaurante3",  "nome restaurante 3", [5, 4, 3], "Descrição restaurante 3", "04:00", ["tag1","tag3","tag6","tag9","tag10"], ["servico1 restaurante3", "servico2 restaurante3"], "Localizacao restaurante 3", ["comentário1 restaurante3","comentário2 restaurante3","comentário3 restaurante3"])
restaurante4 = Atividade( "imagem restaurante4",  "nome restaurante 4", [5, 4, 3], "Descrição restaurante 4", "02:15", ["tag1","tag3","tag6","tag9","tag10"], ["servico1 restaurante4", "servico2 restaurante4"], "Localizacao restaurante 4", ["comentário1 restaurante4","comentário2 restaurante4","comentário3 restaurante4"])
restaurante5 = Atividade( "imagem restaurante5",  "nome restaurante 5", [5, 4, 3], "Descrição restaurante 5", "02:30", ["tag1","tag3","tag6","tag9","tag10"], ["servico1 restaurante5", "servico2 restaurante5"], "Localizacao restaurante 5", ["comentário1 restaurante5","comentário2 restaurante5","comentário3 restaurante5"])
restaurantes = [restaurante1,restaurante2,restaurante3,restaurante4,restaurante5]



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


# def escolherPraias():
# def escolherPasseios():
# def escolherRestaurantes():
#     #obs tem o filtro tambem. ##filtraAtividade(listaAtividades, tags):##
#     for praia in praias:
#         print(f"{praia.nome} --- digite [{index}]")
#     print("qual praia voce quer ver?")
#     print("Quer curtir alguma praia?")
#     print("quer ver os filtros?") 

# def verPraia():
#     print(praiaTal)
#     #obs: so pode fazer isso quando logado == True
#         print("voce quer adicionar ela ao seu roteiro?")
#         print("Para qual roteiro voce quer adicionar")
#               adicionarRoteiro(numRoteiro, atividade)                   
#         print("voce quer cutir essa praia?")
#         print("voce quer fazer um comentario?")

# def filtrar(praias[]):
#     print("quer filtrar por isso?")
#     print("quer filtrar por aquilo?")
#     if tem a tag do filtro -> praias[].tags
#         verPraias(praiasFiltradas[])


# verPerfil() #obs criar tambem um perfil de admin.
# escolherPraias() #printar todas praias, todos passeios e todos restaurantes, engloba: escolherRestaurantes()
# escolherPasseios() #printar todos passeios
# escolherRestaurantes() #printar todos restaurantes
# verPraia() #printar todas informações da praia


    

def verPasseio():
    while True:
        print("Escolha a opção desejada: ")
        print("1 para adicionar esse passeio ao seu roteiro")
        print("2 para curtir esse passeio")
        print("3 para fazer um comentário sobre ele")
        print("0 para voltar para ver outras opções de passeios")
        
        escolha = (int(input()))
        
        if escolha == 1:
           adicionarRoteiro()
        
        if escolha == 2:
            criarRoteiro()
           # curtir()
            
        #if escolha == 3:
           # fazComentario()
            
        if escolha == 0:
            escolherPasseio()

filtros = ["Bom para crianças", "Natureza", "aventura", "para Casais", "Pet friendly", "praia", "bom para idosos"]

def filtrar(filtros):
    filtrosEscolhidos = []
    print("Selecione o filtro que você deseja aplicar para passeios: ")
    for i in range(len(filtros)):
        print(f"[{i+1}] - {filtros[i]}")
    for i in range(2):
        valorEscolhido = int(input())
        if(valorEscolhido == 0):  
            break
        filtrosEscolhidos.append(filtros[valorEscolhido-1])
    teste = pesquisar(filtrosEscolhidos, passeios)
    for test in teste:
        print(test.nome)

def escolherPasseio(passeios): 
    print("Escolha o passeio que você quer ver: ")
    print("[-1] - Filtrar passeios")
    print("[0] - para voltar para as opções")
    for i in range(len(passeios)):
        print(f"[{i+1}] - {passeios[i]}")
    valorEscolhido = int(input())
    print(passeios[i].nome)
    if(valorEscolhido == 0):  
        main()
    if valorEscolhido == -1:
        filtrar()   
            
    
def main():
    while True:
        print("Escolha a opção desejada: ")
        print("1 para entrar em seu perfil\n2 para ver roteiros")
        print("3 para ver praias\n4 para ver passeios")
        print("5 para ver restaurantes\n6 para ver roteiros curtidos por outros viajantes como você")
        print("7 para ver atrações populares\n8 para usar a ferramenta de pesquisa")
        goTo = int(input())

        if goTo == 1:
            #verPerfil()
            return
        if goTo == 2:
            #verRoteiros()
            return
        if goTo == 3:
            #verPraias()
            return
        if goTo == 4:
            escolherPasseio(passeios)
            return
        if goTo == 5:
            #verRestaurantes()
            return
        if goTo == 6:
            #RoteirosOutrosViajantes()
            return
        if goTo == 7:
            #AtracoesPopulares()
            return
        if goTo == 8:
            #fazerPesquisa()
            return
            
main()            

#class Quiz:
    #def __init__(self,)
    
        
# verRestaurante() #printar todas informaçoes do restaurante
# adicionarAoRoteiro() #adiciona a atividade selecionada para um roteiro.
# curtirAtividade() #adiciona a atividade curtida a uma lista de atividades curtidas pelo usuario
# fazerComentario() #recebe um usuario que da uma nota 0-5 estrelas (tem que alterar a média da nota do passeio) e adicionar o comentario à uma lista de comentarios da atividade.
# filtrar() #recebe as tags que o usuario quer filtrar (obs: um valor para cada filtro selecionado.), compara com as tags da atividade e retorna uma lista de atividades que possuem as tags selecionadas.
# fazerPesquisa() #recebe um input do usuario e faz a pesquisa dele.
