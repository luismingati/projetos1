
def verRestaurantes(restaurantes):
  print("------------------------")  
  for i in range(len(restaurantes)):
    print(f"Digite [{i+1}] para visualizar")
    print(restaurantes[i].imagem)
    print()
    print(f"{restaurantes[i].nome} - {restaurantes[i].calculaNota()}")
    print()
    print("------------------------")

def visualizarRestaurante(visualizar, retorno):
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
    acao = int(input())
    if acao == 0:
      verRestaurantes(retorno)
    if acao ==1:
      pass
      #adicionaROteiro()
    if acao == 2:
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
