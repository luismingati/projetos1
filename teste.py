class Aluno:
    def __init__(self, nome, idade, cpf, filmes):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.filmes = filmes
    
    def __str__(self):
        return "self.nome"

luis = {
    "nome":"luis otavio",
    "idade": 21,
}

 
luis = Aluno("luis otavio", 21, "1123124124", ["terror", "aventura", "romance"])
isabela = Aluno("Isabela", 18, "341235113",["terror", "acao"])

pessoas = [luis, isabela]
filtragem = ["terror", "romance"]
arrayFiltrado = []
contador = 0
for pessoa in pessoas:
    contador = 0
    for filtro in filtragem:
        if filtro in pessoa.filmes:
            contador += 1
    if len(filtragem) == contador:
        arrayFiltrado.append(pessoa)
        print("teste")

print(arrayFiltrado)