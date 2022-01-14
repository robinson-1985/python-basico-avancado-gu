'''
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

Zem of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythonica.

1) - Utiliza Camel Case para o nome de classes:

Exemplo: 

class Calculadora:
    pass

class CalculadoraCientifica:
    pass

2) - Utiliza nomes minúsculos, separados por underline para funções ou variáveis.

Exemplo: 

def soma_dois():
    pass

numero = 4

numero_impar = 5


3) - Utilize 4 espaços para identação!

if 'a' in 'banana':
    print('tem')

4) - Linhas em branco

- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

5) - Imports 

imports sempre devem serem feitos em linhas separadas:

exemplo:

- Import Errado 

import sys, os

- Import certo

import sys
import os

Não há problemas em utilizar:

from types import StringType, ListType

- Caso tenha muito imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

- Imports devem ser colocados no tpo do arquivo, logo depois de quaisquer comentários 
ou docstrings e antes de constantes ou variáveis globais.


6) - Espaços em expresões e instruções

*****Não faça isto:

funcao( algo[ 1 ], { outro: 2 } )

algo (1)

dict ['chave'] = [ indice ]

*****Faça isto:

funcao(algo[1], {outro: 2})

algo(1)

dict['chave'] = [indice]

*****Não faça isto:

x             =1
y             =3
variavel_longa=5

****Faça isto:

x = 1
y = 3
variavel_longa=5

7) - termine sempre um anova instrução com uma nova linha.

'''

import this
