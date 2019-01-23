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
    global criterio, PriC
    if criterio == 'titulo' or 'título':
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

def informação():
    global criterio, ordemtitulo, ordemautor, ordemano
    if config == ['']:
        print("Configuração inexistente\nOrdering Exception")
    else:
        print("Os números na ordenação tem o seguinte significado:")
        print("0 - Indiferente; 1 - Ascendente; 2 - Descendente")
        print("Critério: ", criterio)
        print("Ordenação do título: ", ordemtitulo)
        print("Ordenação do autor: ", ordemautor)
        print("Ordenação do ano de edição: ", ordemano)
    
livros()
config()
    
print("Bem-vindo ao sistema de ordenação!")
print("Aqui você pode ordenar seus livros por título, autor ou ano, com ou sem critério de desempate")
print("Para mudar a ordem, você deve alterar o arquivo de configuração.")
print("Para saber qual ordenação está selecionada, digite 1.\nPara ordenar os livros, digite 2.")
print("Para sair, digite fim.")
while True:
    if config != ['']:
        criterio = config[0]
        ordemtitulo = config[1]
        ordemautor = config[2]
        ordemano = config[3]
    escolha = input("Escolha: ")
    if escolha == '1':
        informação()
    elif escolha == '2':
        if catalogo == ['']:
            print("Não há nenhum livro para ser ordenado.")
        elif config == ['']:
            print("Erro: configuração inexistente.")
        else:
            prioridade(criterio, ordemtitulo, ordemautor, ordemano)
            ordenação()
    elif escolha == "fim":
        break
    else:
        print("Opção inválida, tente novamente.")
