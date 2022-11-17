from verRestaurantes import *


passeioMaragogi = Atividade( "imagem passeio Maragogi",  "Passeio à maragogi", [5, 4, 3], "Saindo de maceió, ao norte, você visitará piscinas naturais", "9h", ["Bom para crianças","Natureza","Praia","Pet friendly", "Bom para idosos"], ["Catamarã", "Apoio no Restaurante pontal do maragogi"], "Pontal do Maragogi, Rodovia AL 101 Norte, Km 130 s/n Burgalhau - Barra Grande, Maragogi - AL, 57799-000, Brazil", [], "passeio")
passeioMarape = Atividade( "imagem passeio Marapé",  "Passeio às Dunas de Marapé", [5, 4, 3], "Paraíso ecológico formado entre a Praia de Duas Barras e o Rio Jequiá. Além disso, pode também visualizar falésias.", "7h", ["Natureza","Aventura"], ["passeio de buggy", "Barraquinha","Day-use", "Circuito Pau-de-Arara", "Trilha dos Caetés"], "Povoado Barra de Jequia SN Duas Barras - Jequiá da Praia - Litoral Sul de Alagoas - 50 min de Maceió, Jequiá da Praia, Alagoas 57244-000 Brasil", [], "passeio")
passeioHibiscus = Atividade( "imagem passeio Hibiscus",  "Passeio à ipipoca no Hibiscus beach club", [5, 4, 3], "Ida a praia de IPIOCA pra aproveitar um dia relaxante no beach club.", "3h30", ["Relaxante","Para casais","Bom para crianças","Natureza","Praia"], ["Passeios Náuticos", "Massagem relaxante","Área HIBISQUINHO para crianças","Passeio de lancha, Stand-up paddling e Caiaque"], "Rodovia AL 101 Norte, Bairro Ipioca Residencial Angra de Ipioca, Maceió, Alagoas 57039-705 Brasil", [], "passeio")

arrayUsuarios = usuarios
arrayAtividades = [passeioMaragogi, passeioHibiscus, passeioMarape]
arrayPasseios = [passeioMaragogi, passeioMarape, passeioHibiscus]
arrayPraias = [passeioMarape, passeioHibiscus]
arrayRestaurantes = [passeioMaragogi, passeioMaragogi]

dictTudo = {
    "usuarios" : arrayUsuarios, 
    "atividades" : arrayAtividades,
    "passeios" : arrayPasseios,
    "praias" : arrayPraias,
    "restaurantes" : arrayRestaurantes,
}
saveData(dictTudo)

archive =  loadData()

usuarios = archive["usuarios"]
passeios = archive["passeios"]
praias = archive["praias"]
restaurantes = archive["restaurantes"]
atividades = archive["atividades"]

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

main()