from data import *
global archive

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.curtidas = []
        self.roteiros = []  

    def fazComentario(self, atividade: object, texto: str, nota: int, imagem: str):
        comentarioAtual = Comentario(self, atividade, texto, nota, imagem)
        listaComentarios = []
        for comentarioAtividade in atividade.comentario:
            listaComentarios.append(comentarioAtividade.usuario_c.email)
        if not atividade.comentario:
            atividade.comentario.append(comentarioAtual)
            atividade.nota.append(nota)
        else:
            if self.email in listaComentarios:
                print("voce ja fez um comentario nessa atividade!")
            else:
                atividade.comentario.append(comentarioAtual)
                atividade.nota.append(nota)

    def curtir(self, atividade):
      global archive
      saveData(archive)
      archive = loadData()
      if(atividade in self.curtidas):
        print("Atividade já foi adicionada")
      else:
        self.curtidas.append(atividade)
        saveData(archive)
        archive = loadData()

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
        else:
          self.roteiros[roteiroSelecionado-1].append(atividade)
          print(f"== atividade adicionada ao roteiro {roteiroSelecionado} ==\n")
          break

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

archive = loadData()