#Bibliotecas
from tabulate import tabulate
from operator import*

#Variáveis 
catalogo = []

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
    
 def titulos(): 
    global catalogo
    titulos = sorted(catalogo, key=itemgetter('titulo'))
    print(tabulate(titulos))
    return titulos

def autor(): 
    global catalogo
    autor = sorted(catalogo, key=itemgetter('autor'))
    print(tabulate(autor))
    return autor

def ano(): 
    global catalogo
    ano = sorted(catalogo, key=itemgetter('ano'), reverse=True)
    print(tabulate(ano))
    return ano
    
livros()
print("Bem-vindo ao sistema de ordenação!")
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
