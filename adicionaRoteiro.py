user = Usuario("nome", "email", "senha", "repeteSenha", "curtidas", [])

def criarRoteiro():
    user.roteiros.append(None)
    print(len(user.roteiros))

def adicionarRoteiro():
    i=0
    quantidadeDeRoteiros = len(user.roteiros)
    print("Escolha o roteiro que você quer?")
    print( "0 - criar roteiro")
    for i in range(quantidadeDeRoteiros):
        print(f"{i+1} - Roteiro {i+1}")
    
    roteiroSelecionado = int(input())
    user.roteiros[i].append(None)
    if roteiroSelecionado == 0:
        criarRoteiro()