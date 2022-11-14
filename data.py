import pickle
from Atividade import Atividade

a1 = Atividade("imagem",  "nome", [1,3 ,5], "descricao", 10, ["tags1","tags2","tags3"], "servicos", "localizacao", [], "passeio")
arrayAtividades = []
arrayAtividades.append(a1)

def saveData(obj, nomeArquivo):
  with open(nomeArquivo, 'wb') as arquivo:
      pickle.dump(obj, arquivo)
      arquivo.close

def loadData(nomeArquivo):
  with open(nomeArquivo, 'rb') as arquivo:
    teste = pickle.load(arquivo)
    arquivo.close
    return teste

teste = loadData("usuarioTeste.pickle")

teste.append(a1)

saveData(teste, "usuarioTeste.pickle")
print(teste)

