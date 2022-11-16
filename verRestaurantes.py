from Usuario import *
from data import *
logado = False
usuarioAtual = None


# u1 = Usuario('luis',"luis","luis")
# u2= Usuario('teste',"teste","teste")
# u3= Usuario('teste2',"teste2","teste2")
# usuarios = [u1,u2,u3]


def verAtividades(atividades, todasAtividades, filtros):
  while True:
    print("------------------------\n")  
    for i in range(len(atividades)):
      print(f"Digite [{i+1}] para visualizar")
      print(atividades[i].imagem)
      print()
      print(f"{atividades[i].nome} - {atividades[i].calculaNota()}")
      print()
      print(f"Categoria: {atividades[i].categoria}")
      print(f"Tags: {atividades[i].tags}")
      print("\n------------------------\n")
    print("[-1] Pesquisar")
    print("[-2] Aplicar Filtros")
    toDo = int(input())
    if toDo > 0:
      visualizarAtividade(atividades[toDo-1], todasAtividades)
    elif toDo == 0: 
      break
    elif toDo == -1:
      pesquisa = input()
      verAtividades(pesquisar(pesquisa, todasAtividades), todasAtividades, filtros)
    elif toDo == -2:
      verAtividades(filtrar(filtros, atividades), todasAtividades, filtros)


def visualizarAtividade(visualizar, todasAtividades):
  global archive
  global usuarioAtual
  while True:
    print("------------------------\n")  
    print(visualizar.imagem)
    print(visualizar.nome)
    print(visualizar.calculaNota())           
    print(visualizar.localizacao)
    print("Descrição: ", visualizar.descricao)
    for tag in visualizar.tags:    
        print(f"{tag}", end=" ")
    #print("Valor médio \n ", valor.estimado)
    #print("Percurso: \n", visualizar.mapa)
    #pontos turisticos visitados
    print(" ")
    print("Avaliações: \n")
    visualizar.verComentarios()
    print("[0] - Voltar")
    print("[-1] - Pesquisar")
    print("[-2] - Fazer Comentário")
    print("[-3] - Adicionar ao Roteiro")
    print("[-4] - Curtir atividade")
    print("[-5] - Abrir navbar")
    print("\n------------------------")
    toDo = int(input())
    if toDo == 0:
      break
    if toDo == -1:
      pesquisa = input()
      verAtividades(pesquisar(pesquisa, todasAtividades), todasAtividades, [''])
    if toDo == -2:
      if not usuarioAtual:
        verPerfil()
      else:
        saveData(archive)
        archive = loadData()
        avaliacao = input(f"Digite aqui sua avaliação para {visualizar.nome}.\n")
        while avaliacao == "":
          print("Digite uma avaliação.")
          avaliacao = input(f"Digite aqui sua avaliação para {visualizar.nome}\n.")
        nota = int(input("Digite sua nota de 0 a 5. Apenas números inteiros.\n"))
        while nota < 0 or nota > 5:
          print("A nota que voce digitou é inválida.")
          nota = int(input("Digite sua nota de 0 a 5. Apenas números inteiros.\n"))
        imagem = input("Poste sua imagem.\n")
        usuarioAtual.fazComentario(visualizar, avaliacao, nota, imagem)
        saveData(archive)
        archive = loadData()
    if toDo == -3:
      if not usuarioAtual:
        verPerfil()
      else:
        saveData(archive)
        archive = loadData()
        usuarioAtual.adicionarAtividadeRoteiro(visualizar)
        saveData(archive)
        archive = loadData()
    if toDo == -4:
      if not usuarioAtual:
        verPerfil()
      else:
        usuarioAtual.curtir(visualizar)
        saveData(archive)
        archive = loadData()
    if toDo == -5:
      navBar()
    
def navBar():
  global usuarioAtual
  while True:
    print("[0] - Voltar")
    print("[1] - Home")
    print("[2] - Meus Roteiros")
    print("[3] - Atividades Curtidas")
    print("[4] - Meu Perfil")
    goTo = int(input())
    if goTo == 0:
      break
    if goTo == 1:
      # main()
      pass
    if goTo == 2:
      if not usuarioAtual:
        verPerfil()
      else:
        print(usuarioAtual.verRoteiros())
    if goTo == 3:
      if not usuarioAtual:
        saveData(archive)
        archive = loadData()
        verPerfil()
        saveData(archive)
        archive = loadData()
      else:
        saveData(archive)
        archive = loadData()
        print(usuarioAtual.verCurtidas())
    if goTo == 4:
      verPerfil()
    
def pesquisar(pesquisa, atividades):
  atividadesFiltradas = []
  if(type(pesquisa) == str):
    for atividade in atividades:
      if pesquisa.lower() == atividade.nome.lower():
        atividadesFiltradas.append(atividade)
      for tag in atividade.tags:
        if tag.lower() == pesquisa.lower():
          atividadesFiltradas.append(atividade)
    if len(atividadesFiltradas) == 0:
      print("Nao encontramos nada relacionado")
    return atividadesFiltradas
  else:
    for item in pesquisa:
      for atividade in atividades:
        for tag in atividade.tags:
          if tag.lower() == item.lower() and atividade not in atividadesFiltradas:
            atividadesFiltradas.append(atividade)
    if len(atividadesFiltradas) == 0:
      print("Nao encontramos nada relacionado")
    return atividadesFiltradas

def verPerfil():
  global logado
  global usuarioAtual
  global usuarios
  global archive
  while True:
    if logado == False:
      print("[1] - Voce ja possui uma conta?")
      print("[2] - Quer criar a sua conta?")
      conta = int(input())
      if conta == 1:
        login = input("Digite Seu email: ")
        senha = input("Digite sua senha: ")
        for usuario in usuarios:
          if usuario.email == login and usuario.senha == senha:
            logado = True
            usuarioAtual = usuario
      else:
        usuarioAtual = Usuario.criaUsusario()
        logado = True
        usuarios.append(usuarioAtual)
        saveData(archive)
        archive = loadData()

    if logado == True:
      print(usuarioAtual.nome)
      print(usuarioAtual.email)
      print(usuarioAtual.senha)
      print("[2] Deslogar")
      print("[1] editar perfil")
      print("[0] voltar")
      goTo = int(input())
      if goTo == 0:
        break
      if goTo == 1:
        novoNome = input("digite seu Nome: ")
        novoEmail = input("Digite seu novo email: ")
        novaSenha = input("digite sua novaSenha: ")
        usuarioAtual.nome = novoNome
        usuarioAtual.email = novoEmail
        usuarioAtual.senha = novaSenha
      if goTo == 2:
        usuarioAtual = None
        logado = False

def filtrar(filtros, atividades):
    filtrosEscolhidos = []
    print("Selecione o(s) filtro(s) que você deseja aplicar: ")
    for i in range(len(filtros)):
        print(f"[{i+1}] - {filtros[i]}")
    for i in range(2):
        valorEscolhido = int(input())
        if(valorEscolhido == 0):  
            break
        filtrosEscolhidos.append(filtros[valorEscolhido-1])
    teste = pesquisar(filtrosEscolhidos, atividades)
    return teste


def todasTags(atividades):
    filtros = []
    for atividade in atividades:
        for filtro in atividade.tags:
            if filtro not in filtros:
                filtros.append(filtro)
            else:
                pass
    return filtros


def bubbleSort(array):
  for i in range(len(array)):
    swapped = False
    for j in range(0, len(array) - i - 1):
      if array[j].calculaNotaInt() < array[j + 1].calculaNotaInt():
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        swapped = True
    if not swapped:
      break	
  return array



# nichos = {1:"Gastronômico", 2:"Cultural", 3:"Natureza", 4:"Família", 5:"Romântico"}

# respostaPerguntas = []

# resposta1 = 0

# def perguntaGastronomica():
#     print("Você prefere uma experiência: ")
#     print("1 - Intimista, como um Bistrô")
#     print("Animada, como um bar")
#     print("Algo rápido, como Fast Food.")
#     print("Um ambiente familiar, como um restaurante")
#     resposta1 = int(input(""))
#     return resposta1

# def perguntaCultural():
#     print("Em relação à cultura, você prefere uma experiência: ")
#     print("Mais artesanal, como uma feira")
#     print("Mais performático, como um concerto ou show")
#     print("Lugares que contam um pouco da história da região alagoense, como Museus e centros históricos")
#     resposta2 = int(input(""))
#     return resposta2
    
# def perguntaNatureza():
#     print("Em relação ao contato com a natureza, você prefere uma experiência: ")
#     print("Desbravadora como uma trilha")
#     print("Relaxante, como uma praia")
#     print("Que permita observar a fauna maceioense e brasileira, como um zoológico")
#     resposta3 = int(input(""))
#     return resposta3

# def perguntaFamilia():
#     print("Em relação à viagem com a família, você prefere uma experiência: ")
#     print("Algo relaxante, como passar o dia na praia.")
#     print("Algo divertido, como ir a um parque aquático.")
#     print("Algo aventureiro, como ir em uma trilha com cachoeira.")
#     resposta4 = int(input(""))
#     return resposta4


# def perguntaRomantica():
#     print("Em relação ao romance, você prefere uma experiência: ")
#     print("Algo mais intimista, como um jantar à luz de velas.")  
#     print("Algo mais aventureiro, como um passeio de caiaque à dois.")
#     resposta5 = int(input(""))
#     return resposta5
    
    
# selecionados = {1 : perguntaGastronomica(), 2: perguntaCultural(), 3: perguntaNatureza(), 4: perguntaFamilia(), 5: perguntaRomantica()}
    
# lista_nichos = []

# def iniciarQuiz():
    
#     print("selecione quias nichos voce gosta: ")
#     print("0 confirmar")
#     for nicho in nichos:
#         print(f"{nicho} {nichos[nicho]}")
#     while True:
#         nicho_selecionado = int(input())
#         if nicho_selecionado != 0:
#             lista_nichos.append(nicho_selecionado)
#         else:
#             break
#     print(lista_nichos)
    
#     for nicho_selecionado in lista_nichos:
#         selecionados[nicho_selecionado]
    



# def quiz(nichos,selecionados):
#     nichoEscolhido = 0
#     print("Escolha os nichos pelos quais você se interessa: ")
#     for i in range(len(nichos)):
#         print(f"[{i+1}] - {nichos[i]}")
#     nichoEscolhido = int(input())
#     selecionados.append(nichoEscolhido)
#     while nichoEscolhido != 0:
#         print("Escolha outro nicho de seu interesse: ")
#         print("Caso não queira selecionar mais nenhum, digite 0.")
#         for i in range(len(nichos)):
#             print(f"[{i+1}] - {nichos[i]}")
#         nichoEscolhido = int(input())
#         selecionados.append(nichoEscolhido)
#         if nichoEscolhido == 0:
#             break
#     nichoEscolhido = int(input())
#     selecionados.append(nichoEscolhido)
