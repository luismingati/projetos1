from data import *

logado = False
usuarioAtual = None
global archive


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.curtidas = []
        self.roteiros = []  

    def curtir(self, atividade):
      global archive
      if(atividade in self.curtidas):
        print("Atividade já foi adicionada")
      else:
        self.curtidas.append(atividade)
        saveData(archive)
        archive = loadData()
        
    def verCurtidas(self):
      if not self.curtidas:
        print("Você ainda não curtiu nenhuma atividade.")
      else:
        print("ATIVIDADES CURTIDAS: ")
        for curtida in self.curtidas:
          print(curtida.nome)

    def verRoteiros(self):
      if not self.roteiros:
        print("Você nao criou roteiros ainda.")
      else:
        cont = 1
        print("------------------------\n")
        for roteiro in self.roteiros:
          print(f"Roteiro {cont}\n")
          for atividade in roteiro:
              print(f"* {atividade.nome}") 
          print("\n------------------------\n") 
          cont+=1

    @staticmethod
    def criaUsusario():
      global archive
      nome = input("insira seu nome: ")
      email = input("insira seu email: ")
      senha = input("insira sua senha: ")
      usuario = Usuario(nome, email, senha) 
      return usuario

    def removeCurtida(self, atividade):
      global archive
      while True:
        if atividade in self.curtidas:
          self.curtidas.remove(atividade)
          saveData(archive)
          archive = loadData()
          break
        

    def adicionarAtividadeRoteiro(self, atividade):
      global archive
      while True:
        cont = 1
        print("Escolha o roteiro que você quer?")
        print( "0 - criar roteiro")
        for roteiro in self.roteiros:
          print(f"{cont} - Roteiro {cont}")
          cont += 1
        roteiroSelecionado = int(input())
        if roteiroSelecionado == 0:
          self.roteiros.append([])
          saveData(archive)
          archive = loadData()
        else:
          self.roteiros[roteiroSelecionado-1].append(atividade)
          print(f"== atividade adicionada ao roteiro {roteiroSelecionado} ==\n")
          saveData(archive)
          archive = loadData()
          break
        

    def fazComentario(self, atividade: object, texto: str, nota: int, imagem: str):
        global archive
        comentarioAtual = Comentario(self, atividade, texto, nota, imagem)
        listaComentarios = []
        for comentarioAtividade in atividade.comentario:
            listaComentarios.append(comentarioAtividade.usuario_c.email)
        if not atividade.comentario:
            atividade.comentario.append(comentarioAtual)
            atividade.nota.append(nota)
            saveData(archive)
            archive = loadData()
        else:
            if self.email in listaComentarios:
                print("voce ja fez um comentario nessa atividade!")
            else:
                atividade.comentario.append(comentarioAtual)
                atividade.nota.append(nota)
                saveData(archive)
                archive = loadData()

class Comentario:
  def __init__(self, usuario_c, atividade_c, texto, nota, imagem):
    self.usuario_c = usuario_c
    self.atividade_c = atividade_c
    self.texto = texto
    self.nota = nota
    self.imagem = imagem

class Atividade:
    def __init__(self, imagem,  nome, nota, descricao, duracaoAtividade, tags, servicos, localizacao, comentario, categoria):
        self.imagem = imagem
        self.nome = nome
        self.nota = nota
        self.descricao = descricao
        self.duracaoAtividade = duracaoAtividade
        self.tags = tags
        self.servicos = servicos
        self.localizacao = localizacao
        self.comentario = comentario
        self.categoria = categoria

    def calculaNota(self):
        return round((sum(self.nota)/len(self.nota))) * "*"

    def calculaNotaInt(self):
        return round((sum(self.nota)/len(self.nota)))

    def verComentarios(self):
        if not self.comentario:
            print("Esta publicacão ainda não tem avaliações\n")
        else:
            print("\n","-"*30,"\n")
            for comentarioUsuario in self.comentario:
                avaliacao = comentarioUsuario.nota * "*"
                print(f"{comentarioUsuario.usuario_c.nome}\t{avaliacao}\n")
                print(f"{comentarioUsuario.texto}\n{comentarioUsuario.imagem}")
                print("\n","-"*30,"\n")

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
        verPerfil()
      else:
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

def bemAvaliadas(atividades):
    atividadesFiltradas = []
    filtrado = bubbleSort(atividades)
    for atividade in filtrado:
        if atividade.calculaNotaInt() > 3:
            atividadesFiltradas.append(atividade)
    return atividadesFiltradas

def main():
    global logado
    global usuarioAtual
    global archive
    while True:
        print("[0] - SAIR")
        print("[1] - PESQUISAR")
        print("[2] - QUIZ")
        print("[3] - CRIE")
        print("[4] - ROTEIROS PRONTOS")
        print("[5] - PASSEIOS")
        print("[6] - RESTAURANTES")
        print("[7] - PRAIAS")
        print("[8] - ATIVIDADES BEM AVALIADAS")
        print("[9] - ATRAÇÕES EM ALTA")
        print("[10] - ABRIR NAVBAR")
        select = int(input())
        if select == 0:
            break
        if select == 1:
            pesquisa = input()
            verAtividades(pesquisar(pesquisa, atividades), atividades, [''])
        if select == 2:
            # iniciarQuiz()
            pass
        if select == 3:
            pass
        if select == 4:
            pass
        if select == 5:
            verAtividades(passeios, atividades, todasTags(passeios))
        if select == 6:
            verAtividades(restaurantes, atividades, todasTags(restaurantes))
        if select == 7:
            verAtividades(praias, atividades, todasTags(praias))
        if select == 8:
            verAtividades(bemAvaliadas(atividades), atividades, todasTags(atividades))
        if select == 9:
            pass
        if select == 10:
            navBar()


archive =  loadData()

usuarios = archive["usuarios"]
passeios = archive["passeios"]
praias = archive["praias"]
restaurantes = archive["restaurantes"]
atividades = archive["atividades"]

main()