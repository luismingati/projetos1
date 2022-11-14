from Usuario import Usuario
logado = False
usuarioAtual = None



u1 = Usuario('luis',"luis","luis","luis",[],[])
u2= Usuario('teste',"teste","teste","teste",[],[])
u3= Usuario('teste2',"teste2","teste2","teste2",[],[])
usuarios = [u1,u2,u3]

def verAtividades(atividades, todasAtividades, filtros):
  while True:
    print("------------------------")  
    for i in range(len(atividades)):
      print(f"Digite [{i+1}] para visualizar")
      print(atividades[i].imagem)
      print()
      print(f"{atividades[i].nome} - {atividades[i].calculaNota()}")
      print()
      print(f"Categoria: {atividades[i].categoria}")
      print(f"Tags: {atividades[i].tags}")
      print("------------------------")
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
  global usuarioAtual
  while True:
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
    if toDo == -3:
      if not usuarioAtual:
        verPerfil()
      else:
        usuarioAtual.adicionarAtividadeRoteiro(visualizar)
    if toDo == -4:
      if not usuarioAtual:
        verPerfil()
      else:
        usuarioAtual.curtir(visualizar)
    if toDo == -5:
      navBar()
    
def navBar():
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
        print(usuarioAtual.roteiros)
    if goTo == 3:
      if not usuarioAtual:
        verPerfil()
      else:
        print(usuarioAtual.curtidas)
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
        print("\tCRIAR CADASTRO")
        nome = input("Digite seu nome")
        email = input("Digite seu melhor email")
        senha = input("Digite sua senha")
        repeteSenha = input("Repita sua senha")
        curtidas = []
        roteiros = []
        usuario = Usuario(nome, email, senha, repeteSenha, curtidas,roteiros)
        usuarioAtual = usuario
        logado = True
        usuarios.append(usuario)
    if logado == True:
      print(usuarioAtual.nome)
      print(usuarioAtual.email)
      print(usuarioAtual.senha)
      print(usuarioAtual.curtidas)
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
        repeteNovaSenha = input("Repita sua nova senha: ")
        usuarioAtual.nome = novoNome
        usuarioAtual.email = novoEmail
        usuarioAtual.senha = novaSenha
        usuarioAtual.repeteSenha = repeteNovaSenha
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