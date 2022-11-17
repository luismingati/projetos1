import pickle

def saveData(obj):
  with open("usuarioTeste.pickle", 'wb') as arquivo:
      pickle.dump(obj, arquivo)
      arquivo.close()
    
def loadData():
  data = []
  with open("usuarioTeste.pickle", 'rb') as arquivo:
    try:
        while True:
            data.append(pickle.load(arquivo))
    except EOFError:
        pass
    return data