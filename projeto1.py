from verRestaurantes import *
from Comentario import *
from Usuario import *
from Atividade import *

praia1 = Atividade( "imagem praia1",  "nome praia 1", [3], "Descrição praia 1", "01:30", ["tag1","tag3","tag6","tag9","tag10"], ["servico1 praia1", "servico2 praia1"], "Localizacao praia 1", [], "praia")
praia2 = Atividade( "imagem praia2",  "nome praia 2", [0], "Descrição praia 2", "02:30", ["tag1","tag2","tag3","tag4","tag5"], ["servico1 praia2", "servico2 praia2"], "Localizacao praia 2", [], "praia")
praia3 = Atividade( "imagem praia3",  "nome praia 3", [1], "Descrição praia 3", "00:30", ["tag2","tag4","tag6","tag8","tag10"], ["servico1 praia3", "servico2 praia3"], "Localizacao praia 3", [], "praia")
praia4 = Atividade( "imagem praia4",  "nome praia 4", [2], "Descrição praia 4", "01:00", ["tag1","tag2","tag4","tag5","tag9"], ["servico1 praia4", "servico2 praia4"], "Localizacao praia 4", [], "praia")
praia5 = Atividade( "imagem praia5",  "nome praia 5", [5, 5, 5], "Descrição praia 5", "03:00", ["tag1","tag3","tag5","tag7","tag9"], ["servico1 praia5", "servico2 praia5"], "Localizacao praia 5", [], "praia")
praias = [praia1, praia2, praia3, praia4, praia5]

passeioMaragogi = Atividade( "imagem passeio Maragogi",  "Passeio à maragogi", [5, 4, 3], "Saindo de maceió, ao norte, você visitará piscinas naturais", "9h", ["Bom para crianças","Natureza","Praia","Pet friendly", "Bom para idosos"], ["Catamarã", "Apoio no Restaurante pontal do maragogi"], "Pontal do Maragogi, Rodovia AL 101 Norte, Km 130 s/n Burgalhau - Barra Grande, Maragogi - AL, 57799-000, Brazil", [], "passeio")
passeioMarape = Atividade( "imagem passeio Marapé",  "Passeio às Dunas de Marapé", [5, 4, 3], "Paraíso ecológico formado entre a Praia de Duas Barras e o Rio Jequiá. Além disso, pode também visualizar falésias.", "7h", ["Natureza","Aventura"], ["passeio de buggy", "Barraquinha","Day-use", "Circuito Pau-de-Arara", "Trilha dos Caetés"], "Povoado Barra de Jequia SN Duas Barras - Jequiá da Praia - Litoral Sul de Alagoas - 50 min de Maceió, Jequiá da Praia, Alagoas 57244-000 Brasil", [], "passeio")
passeioHibiscus = Atividade( "imagem passeio Hibiscus",  "Passeio à ipipoca no Hibiscus beach club", [5, 4, 3], "Ida a praia de IPIOCA pra aproveitar um dia relaxante no beach club.", "3h30", ["Relaxante","Para casais","Bom para crianças","Natureza","Praia"], ["Passeios Náuticos", "Massagem relaxante","Área HIBISQUINHO para crianças","Passeio de lancha, Stand-up paddling e Caiaque"], "Rodovia AL 101 Norte, Bairro Ipioca Residencial Angra de Ipioca, Maceió, Alagoas 57039-705 Brasil", [], "passeio")
passeios = [passeioMaragogi, passeioMarape, passeioHibiscus]

restaurante1 = Atividade( "imagem restaurante1",  "nome restaurante 1", [5, 4, 3], "Descrição restaurante 1", "01:30", ["tag1","tag3","tag6","tag9","tag10"], ["servico1 restaurante1", "servico2 restaurante1"], "Localizacao restaurante 1", [], "restaurante")
restaurante2 = Atividade( "imagem restaurante2",  "nome restaurante 2", [5, 4, 3], "Descrição restaurante 2", "02:15", ["tag1","tag3","tag6","tag9","tag10"], ["servico1 restaurante2", "servico2 restaurante2"], "Localizacao restaurante 2", [], "restaurante")
restaurante3 = Atividade( "imagem restaurante3",  "nome restaurante 3", [5, 4, 3], "Descrição restaurante 3", "04:00", ["tag1","tag3","tag6","tag9","tag10"], ["servico1 restaurante3", "servico2 restaurante3"], "Localizacao restaurante 3", [], "restaurante")
restaurante4 = Atividade( "imagem restaurante4",  "nome restaurante 4", [5, 4, 3], "Descrição restaurante 4", "02:15", ["tag1","tag3","tag6","tag9","tag10"], ["servico1 restaurante4", "servico2 restaurante4"], "Localizacao restaurante 4", [], "restaurante")
restaurante5 = Atividade( "imagem restaurante5",  "nome restaurante 5", [5, 4, 3], "Descrição restaurante 5", "02:30", ["tag1","tag3","tag6","tag9","tag10"], ["servico1 restaurante5", "servico2 restaurante5"], "Localizacao restaurante 5", [], "restaurante")
restaurantes = [restaurante1,restaurante2,restaurante3,restaurante4,restaurante5]
atividades = [praia1,praia2,praia3,praia4,praia5, restaurante1,restaurante2,restaurante3,restaurante4, restaurante5, passeioHibiscus,passeioMaragogi]


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
