# SumOne-Challenge
Repositório com minha solução para o challenge dado à mim pela SumOne como parte do processo seletivo para estágio em web development.

Challenge: Serviço de Ordenação
Linguagem utilizada: Python 3.7 - 64 bits

  O Serviço de Ordenação tem o objetivo de organizar os livros em uma biblioteca. Ele possui mais de 50 possibilidades de ordenação, dando ao usuário a chance de escolher sua preferência.
O programa deve ser executado pelo Prompt de Comando do seu computador. O próprio Prompt exibirá a interface do programa.

                                            -- INSTRUÇÕES PARA EXECUÇÃO --
  Você precisará ter a versão mais atual de Python instalada em seu computador, caso deseje executar/alterar o código fonte. Você pode encontrar Python em https://www.python.org/downloads/. No processo de instalação, não esqueça de adicionar Python ao PATH, essa opção está disponível no próprio instalador. Ou caso deseje, utilize a IDE de sua preferência.
  Você precisará instalar as bibliotecas que foram utilizadas no programa, operator e tabulate. Para isso, instale o PIP. Após instalar o Python e adicioná-lo ao PATH, abra o prompt de comando e digite 'python -m ensurepip' sem as aspas. Após, digite 'python -m ensurepip --upgrade' também no console para garantir a última versão do PIP. 

                                                   -- BIBLIOTECAS --
  Foram utilizadas duas bibliotecas do Python neste programa:
 
- operator -> foi utilizado um recurso desta biblioteca chamado "itemgetter". Ele pega um item do dicionário de acordo com sua "key".
- tabulate -> cria o output no formato de tabela.

  Para instalar ambas, abra o prompt de comando e digite 'pip install operator' e 'pip install tabulate'. Em caso de erro, você deverá instalar ambos manualmente. Busque o arquivo no formato 'wheel', de ambas as bibliotecas. Você pode encontrar um tutorial de como fazer esta instalação manualmente com facilidade no Google.

                                                    -- ARQUIVO .EXE --
  Este programa também está disponível no formato .exe, como um aplicativo. Alterações feitas no código não irão afetar o aplicativo, porém alterações nos arquivos catalogo.txt e config.txt irão. 

                                               -- ALTERANDO OS LIVROS --
  Dentro da pasta com o executável existe um arquivo chamado 'catalogo.txt'. Nele, estão os livros a serem organizados. Esta lista pode ser alterada da forma que o usuário desejar, com adição ou remoção de títulos, desde que o formato seja obedecido:
  
  Número - Título - Autor - Ano da Edição.
  
  Para que o programa contabilize a alteração, ela deve ser feita antes que o programa seja executado.

                                           -- ALTERANDO AS CONFIGURAÇÕES --
  O usuário possui a opção de alterar as configurações de ordenação da forma como preferir. Dentro da pasta também existe um arquivo chamado 'config.txt'. Nele, estão as configurações que serão lidas pelo programa. Para fazer alterações, basta o usuário escolher a preferência de ordenação, esta configuração irá priorizar uma palavra chave dentre as outras, e a ordem de ordenação do título, autor e ano. Para preferência de ordenação, o usuário deverá escolher entre título, autor e ano. Para ordem de ordenação, deverá escolher entre: 
  
  0 - indiferente, 1 - ascendente, 2 - descendente.
  
  O arquivo .txt deverá ser organizado da seguinte forma:
  
    Preferência de ordenação; 
    Ordem de ordenação do título; 
    Ordem de ordenação do autor; 
    Ordem de ordenação do ano.
    
  Caso o usuário não queira ordenar os livros, basta deixar o arquivo config.txt em branco.

                                                  -- RESULTADOS --
  O programa ordenará os livros de acordo com a escolha do usuário. O resultado da ordenação será exibido em forma de tabela.
  
EXEMPLO:

  Para obter o resultado de ordenação por ano e autor descendente e título ascendente, a configuração do arquivo deve ser feita da seguinte forma:

Preferência de ordenação: título

Ordem de ordenação do título: 1

Ordem de ordenação do autor: 2

Ordem de ordenação do ano: 2

   O resultado será:
-  -----------------------------------------------  -----------------  ----
4  Internet & World Wide Web: How to Program        Deitel&Deitel      2007

1  Java How to Program                              Deitel&Deitel      2007

3  Head First Design Patterns                       Elisabeth Freeman  2004

2  Patterns of Enterprise Application Architecture  Martin Fowler      2002
-  -----------------------------------------------  -----------------  ---- 

  Título será a forma de diferenciação entre livros com mesmo autor e ano, neste caso. 
