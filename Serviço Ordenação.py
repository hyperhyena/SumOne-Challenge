#Bibliotecas
from tabulate import tabulate
from operator import*

#Variáveis 
catalogo = []
config = []

#Funções
def livros():
    biblio = {}
    with open('catalogo.txt') as temp:
        for line in temp:
            livrotemp = (line.rstrip("\n\t"))
            livro = livrotemp.split(" - ")
            new=biblio.copy()
            new["indice"] = livro[0]
            new["titulo"] = livro[1]
            new["autor"] = livro[2]
            new["ano"] = livro[3]
            catalogo.append(new)
    return catalogo

def config():
    global config
    arquivo = open("config.txt", "r")
    config = arquivo.read().split("\n")
    arquivo.close
    return config

def prioridade(cri, orT, orAu, orAn):
    global catalogo, PriC
    if cri == 'titulo':
        if orT == '1':
            PriC = sorted(catalogo, key=itemgetter('titulo'))
        elif orT == '2':
            PriC = sorted(catalogo, key=itemgetter('titulo'), reverse=True)
    if cri == 'autor':
        if orAu == '1':
            PriC = sorted(catalogo, key=itemgetter('autor'))
        elif orAu == '2':
            PriC = sorted(catalogo, key=itemgetter('autor'), reverse=True)
    if cri == 'ano':
        if orAn == '1':
            PriC = sorted(catalogo, key=itemgetter('ano'))
        if orAn == '2':
            PriC = sorted(catalogo, key=itemgetter('ano'), reverse=True)
    print(tabulate(PriC))
    return PriC
  
 def ordenação():
    global Oa, Ob, Na, Nb, PriC
    if Na and Nb != '0':
        if Na and Nb == '1':
            ordemF = sorted(PriC, key=itemgetter(Oa,Ob))
        elif Na and Nb == '2':
            ordemF = sorted(PriC, key=itemgetter(Ob,Oa), reverse=True)
        elif Na == '1' and Nb == '2':
            ordemI = sorted(PriC, key=itemgetter(Oa))
            ordemF = sorted(ordemI, key=itemgetter(Ob), reverse=True)
        elif Na == '2' and Nb == '1':
            ordemI = sorted(PriC, key=itemgetter(Oa), reverse=True)
            ordemF = sorted(ordemI, key=itemgetter(Ob))
    if Na == '0' and Nb != '0':
        if Nb == '1':
                ordemF = sorted(PriC, key=itemgetter(Ob))
        elif Nb == '2':
                ordemF = sorted(PriC, key=itemgetter(Ob), reverse=True)
    if Na != '0' and Nb == '0':
        if Na == '1':
                ordemF = sorted(PriC, key=itemgetter(Oa))
        elif Na == '2':
                ordemF = sorted(PriC, key=itemgetter(Oa), reverse=True)
    elif Na and Nb == '0':
        ordemF = PriC
    print(tabulate(ordemF))
    return ordemF
    
livros()
config()

criterio = config[0]
ordemtitulo = config[1]
ordemautor = config[2]
ordemano = config[3]

if criterio == 'titulo':
    Oa = 'autor'
    Ob = 'ano'
    Na = ordemautor
    Nb = ordemano
elif criterio == 'autor':
    Oa = 'titulo'
    Ob = 'ano'
    Na = ordemtitulo
    Nb = ordemano
elif criterio == 'ano':
    Oa = 'titulo'
    Ob = 'autor'
    Na = ordemtitulo
    Nb = ordemautor
    
print("Bem-vindo ao sistema de ordenação!")
prioridade(criterio, ordemtitulo, ordemautor, ordemano)   
ordenação()
while True:
    if catalogo == []:
        print("Não há nenhum livro para ser ordenado.")
        break
    elif catalogo != []:
        print("Como você deseja ordenar estes livros?")
        print("1 - Título")
        print("2 - Autor")
        print("3 - Ano")
        print("Caso deseje sair, digite fim.")
        criterio = input("Número do critério: ")
        if criterio == "":
            print("Não foi selecionada nenhuma opção.")
            print("Ordering Exception")
        if criterio == "1":
            print("A ordernação por título é apenas ascendente.")
            titulos('a')
        if criterio == "2":
            print("A ordernação por autores é ascendente.")
            autor('a')
        if criterio == "3":
            print("A ordernação por ano é descendente.")
            ano()
        if criterio == "fim":
            break
        else:
            print("Opção inválida, tente novamente.")
