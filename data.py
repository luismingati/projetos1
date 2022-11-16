import pickle

def saveData(obj):
  with open("usuarioTeste.pickle", 'wb') as arquivo:
      pickle.dump(obj, arquivo)
      arquivo.close()
    
def loadData():
  with open("usuarioTeste.pickle", 'rb') as arquivo:
    arquive = pickle.load(arquivo)
    arquivo.close()
    return arquive