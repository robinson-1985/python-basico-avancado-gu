'''
Loop for

Loop -> Estruturas de repetição.
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.

Exe. de iteráveis:
- String
    nome = 'Geek University'

Lista
    lista = [1,3,5,7,9]

Range
    numeros = range(1, 10)

nome = 'Geek University'
lista = [1,3,5,7,9]
numeros = range(1, 10) # Temos que transformar em uma lista
#Exemplo de for 1 (iterando sobre uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (iterando sobre um range)

range(valor_iniciar, valor_final)
Obs: o valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não entra.

for numero in range(1, 10):
    print(numero)

--> Enumerate: ((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' ')...)

for i, v in enumerate(nome):
    print(nome[i])


for indice, letra in enumerate(nome):
    print(nome[indice])

for _, letra in enumerate(nome):
    print(nome[letra])

Obs: quando não precisamos de um valor, podemos descartá-lo utilizando um underline(_)

for valor in enumerate(nome):
    print(valor)

for i, valor in enumerate(nome):
    print(nome[i])

nome = 'Geek University'
lista = [1,3,5,7,9]
numeros = range(1, 10) # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor[1])

---> Soma de loop

quantidade = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, quantidade+1):
    num = int(input(f'Informe o {n}/{quantidade} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

Explicação: o Python por default coloca \n, então para que não pule linha colocamos
end=' '

nome = 'Geek University'
for letra in nome:
    print(letra, end='')

Tabela de Emojis unicode: https://apps.tmwithlock.info/emoji/tables/unicode

'''

# Original: U+1F60D
# Modificado: U0001F60D

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)

