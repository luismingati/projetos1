import os
os.system("cls")


class Usuario:
    def _init_(self, nome, email, senha, repeteSenha, curtidas, roteiros):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.repeteSenha = repeteSenha
        self.curtidas = curtidas
        self.roteiros = roteiros  

    def fazComentario(self, atividade, texto, nota, imagem):
        return
    
    def curtir(self, atividade):
        return

    def adicionarRoteiro(self, atividade):
        return
    
    
class Atividade:
    def _init_(self, imagem,  nome, nota, descricao, duracaoAtividade, tags, servicos, localizacao, comentario):
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

passeioMaragogi = Atividade( "imagem passeio1",  "Passeio à maragogi", [5, 4, 3], "Saindo de maceió, ao norte, você visitará piscinas naturais", "9h", ["Bom para crianças","Natureza","Praia inclusa","Pet friendly, Bom para idosos"], ["Catamarã", "Apoio no Restaurante pontal do maragogi"], "Pontal do Maragogi, Rodovia AL 101 Norte, Km 130 s/n Burgalhau - Barra Grande, Maragogi - AL, 57799-000, Brazil", ["Passeio com preço justo","Guias divertidos e engraçados","Ótimo serviço prestado"])
passeioMarape = Atividade( "imagem passeio2",  "Passeio às Dunas de Marapé", [5, 4, 3], "Paraíso ecológico formado entre a Praia de Duas Barras e o Rio Jequiá. Além disso, pode também visualizar falésias.", "7h", ["Natureza","Aventura"], ["passeio de buggy", "Barraquinha","Day-use", "Circuito Pau-de-Arara", "Trilha dos Caetés"], "Povoado Barra de Jequia SN Duas Barras - Jequiá da Praia - Litoral Sul de Alagoas - 50 min de Maceió, Jequiá da Praia, Alagoas 57244-000 Brasil", ["comentário1 passeio2","comentário2 passeio2","comentário3 passeio2"])
passeioBarco = Atividade( "imagem passeio3",  "nome passeio 3", [5, 4, 3], "Descrição passeio 3", "04:00", ["tag1","tag3","tag6","tag9","tag10"], ["servico1 passeio3", "servico2 passeio3"], "Localizacao passeio 3", ["comentário1 passeio3","comentário2 passeio3","comentário3 passeio3"])
passeioHibiscus = Atividade( "imagem passeio4",  "nome passeio 4", [5, 4, 3], "Descrição passeio 4", "02:15", ["tag1","tag3","tag6","tag9","tag10"], ["servico1 passeio4", "servico2 passeio4"], "Localizacao passeio 4", ["comentário1 passeio4","comentário2 passeio4","comentário3 passeio4"])
passeioMilagres = Atividade( "imagem passeio5",  "nome passeio 5", [5, 4, 3], "Descrição passeio 5", "02:30", ["tag1","tag3","tag6","tag9","tag10"], ["servico1 passeio5", "servico2 passeio5"], "Localizacao passeio 5", ["comentário1 passeio5","comentário2 passeio5","comentário3 passeio5"])
passeioBuggy = Atividade( "imagem passeio5",  "nome passeio 5", [5, 4, 3], "Descrição passeio 5", "02:30", ["tag1","tag3","tag6","tag9","tag10"], ["servico1 passeio5", "servico2 passeio5"], "Localizacao passeio 5", ["comentário1 passeio5","comentário2 passeio5","comentário3 passeio5"])
passeios = [passeioMaragogi, passeioMarape, passeioBarco, passeioHibiscus, passeioMilagres, passeioBuggy]

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
# verPraia() #printar todas informações da pria,
def verPasseio():
    while True:
        print("Escolha a opção desejada: ")
        print("1 para adicionar esse passeio ao seu roteiro")
        print("2 para curtir esse passeio")
        print("3 para fazer um comentário sobre ele")
        print("0 para voltar para ver outras opções de passeios")
        
        escolha = (int(input()))
        
        #if escolha == 1:
           # adicionarRoteiro()
        
        #if escolha == 2:
           # curtir()
            
        #if escolha == 3:
           # fazComentario()
            
        if escolha == 0:
            escolherPasseio()

def escolherPasseio(): 
    while True:
        print("Escolha o passeio que você quer ver: [0 para voltar para as opções]")
        print("1: Passeio à maragogi")
        print("2: Passeio às Dunas de Marapé")
        print("3: Passeio de Barco")
        print("4: Passeio ao Hibiscus Beach Club")
        print("5: Passeio à São Miguel dos Milagres")
        print("6: Passeio de Buggy nas Praias do litoral Sul")
        print("0 para voltar para a aba inicial")
        
        numero = int(input())
        
        if numero == 1:
            print(passeioMaragogi)
            verPasseio()
        if numero == 2:
            print(passeioMarape)
            verPasseio()
        if numero == 3:
            print(passeioBarco)
            verPasseio()
        if numero == 4:
            print(passeioHibiscus)
            verPasseio()
        if numero == 5:
            print(passeioMilagres)
            verPasseio()
        if numero == 6:
            print(passeioBuggy)
            verPasseio()
        if numero == 0:
            main()
    
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
            escolherPasseio()
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

        
        
        
# verRestaurante() #printar todas informaçoes do restaurante
# adicionarAoRoteiro() #adiciona a atividade selecionada para um roteiro.
# curtirAtividade() #adiciona a atividade curtida a uma lista de atividades curtidas pelo usuario
# fazerComentario() #recebe um usuario que da uma nota 0-5 estrelas (tem que alterar a média da nota do passeio) e adicionar o comentario à uma lista de comentarios da atividade.
# filtrar() #recebe as tags que o usuario quer filtrar (obs: um valor para cada filtro selecionado.), compara com as tags da atividade e retorna uma lista de atividades que possuem as tags selecionadas.
# fazerPesquisa() #recebe um input do usuario e faz a pesquisa dele.