import os
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
    print("[0] - Voltar")
    print("[1] - Adicionar ao Roteiro")
    print("[2] - Fazer Comentário")
    print("[-1] - Pesquisar")
    toDo = int(input())
    if toDo == 0:
      break
    if toDo == -1:
      pesquisa = input()
      verAtividades(pesquisar(pesquisa, todasAtividades), todasAtividades, [''])
    if toDo == -2:
      pass
      #fazCOmentario()
    #print((nome.imagem.login),"",alcculaNota(),"\n",texto)

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

def verPerfil(usuario):
  while True:
    if usuario.logado == False:
      print("[1] - Voce ja possui uma conta?")
      print("[2] - Quer criar a sua conta?")
      conta = int(input())
      if conta == 1:
        login = input("Digite Seu login: ")
        senha = input("Digite sua senha: ")
        if usuario.email == login and usuario.senha == senha:
          usuario.logado = True
      else:
        print("nao temos isso hehe")
    if usuario.logado == True:
      print(usuario.nome)
      print(usuario.email)
      print(usuario.roteiros)

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
