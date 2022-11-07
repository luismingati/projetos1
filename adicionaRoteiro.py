user = Usuario("nome", "email", "senha", "repeteSenha", "curtidas", [])

def criarRoteiro(usuario):
    usuario.roteiros.append(None)
    print(len(usuario.roteiros))

def adicionarRoteiro(atividade):
    i=0
    quantidadeDeRoteiros = len(user.roteiros)
    print("Escolha o roteiro que você quer?")
    print( "0 - criar roteiro")
    for i in range(quantidadeDeRoteiros):
        print(f"{i+1} - Roteiro {i+1}")
    
    roteiroSelecionado = int(input())
    user.roteiros[i].append(atividade)
    if roteiroSelecionado == 0:
        criarRoteiro()