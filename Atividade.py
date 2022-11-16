
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
