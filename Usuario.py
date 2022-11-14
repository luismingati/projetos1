from Comentario import Comentario


class Usuario:
    def __init__(self, nome, email, senha, repeteSenha, curtidas, roteiros):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.repeteSenha = repeteSenha
        self.curtidas = curtidas
        self.roteiros = roteiros  

    def curtir(self, atividade):
      while True:
        if(atividade in self.curtidas):
          print("Atividade já foi adicionada")
          break
        else:
          self.curtidas.append(atividade)
          break
      

    def removeCurtida(self, atividade):
      while True:
        if atividade in self.curtidas:
          self.curtidas.remove(atividade)
          break
        

    def adicionarAtividadeRoteiro(self, atividade):
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
