class Usuario:
    def __init__(self, nome, email, senha, senhaRepetida):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.senhaRepetida = senhaRepetida

def start():
    while True:
        print("Digite onde voce quer ir.")
        print("1 - Ver Perfil")
        print("2 - Criar um roteiro personalizado")
        print("3 - Ver Praias")
        print("4 - Ver passeios")
        print("5 - Ver restaurantes")
        opcao = int(input())
        
        if(opcao == 1):
            perfil()
            return
        if( opcao == 2):
            #roteiroPersonalizado()
            return
        if opcao == 3:
            praias()
            return
        if(opcao == 4):
            passeios()
            return
        if(opcao == 5):
            restaurantes()
            return

usuario = Usuario(None, None, None, None)
login = False

def perfil():
    global login
    global usuario
    while True:
        if(login == False):
            print("Voce ja possui uma conta?\n[0] - Voltar\n[1] - Sim\n[2] - Não")
            conta = int(input())
            if(conta == 1):
                email = input("Digite seu email")
                senha = input("Digite sua senha")
                if(usuario.email == email and usuario.senha == senha):
                    login = True
                    return
            if(conta == 2):
                if(usuario):
                    print("CRIAR CONTA")
                    nome = input("Digite seu nome")
                    email = input("Digite seu Email")
                    senha = input("Digite seu senha")
                    senhaRepetida = input("Digite sua senha novamente")
                    usuario = Usuario(nome, email, senha, senhaRepetida)
                    login = True
        if(login == True):
            print("VOCE ESTA LOGADO")
            print(usuario.nome)
            return


def praias():
    while True:
        print("Qual praia voce quer ver? [ 0 PARA VOLTAR ]")
        print("1 - Praia de boa Viagem")
        print("2 - Praia de Setúbal")
        print("3 - Porto de galinhas")
        print("4 - Copacabana")
        opcao = int(input())
        if opcao == 1:
            print("PRAIA DE BOA VIAGEM [ 0 PARA VOLTAR ]")
            print('Praia localizada em boa viagem recife')
            print("***imagem***")
            print("como chegar? - Digite 1 (obs: Sai do app)")
            options = int(input())
            if(options == 0):
                praias()
            else:
                print("maps.google.com")
                break
        elif opcao == 0:
            start()

def passeios():
    while True:
        print("Qual passeio voce quer fazer? [ 0 PARA VOLTAR ]")
        print("1 - Passeio de buggy")
        print("2 - Passeio de lancha")
        print("3 - Passeio de cavalo")
        print("4 - Passeio de burro")
        opcao = int(input())
        if opcao == 1:
            print("PASSEIO DE BUGGY [ 0 PARA VOLTAR ]")
            print('Passeio de buggy na lagoa da anta! voce pode trazer sua criança que ela vai ficar muito feliz!')
            print("***imagem***")
            print("Contato - Digite 1 (obs: Sai do app)")
            options = int(input())
            if(options == 0):
                passeios()
            else:
                print("(81) 992673319 ")
                break
        elif opcao == 0:
            start()

def restaurantes():
    while True:
        print("Qual restaurante voce quer conhecer? [ 0 PARA VOLTAR ]")
        print("1 - Coco Bambu")
        print("2 - Restaurante da Anta")
        print("3 - Dona Gula")
        print("4 - Cinema")
        opcao = int(input())
        if opcao == 1:
            print("COCO BAMBU [ 0 PARA VOLTAR ]")
            print('Restaurante feito pra sua familia! Casais tambem!')
            print("***imagem***")
            print("Como chegar - Digite 1 (obs: Sai do app)")
            print("Ligar para fazer reserva - Digite 2 (obs: Sai do app)")
            options = int(input())
            if(options == 0):
                restaurantes()
            elif(options == 1):
                print("Rua tal e tal")
                break
            elif(options == 2):
                print("(81) 992673319")
                break
        elif opcao == 0:
            start()

start()