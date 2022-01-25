'''
Loop while

Forma geral:

while expressão_booleana:
    //execução do loop

Condição de parada: O bloco do while será repetido enquanto a expressão booleana for 
verdadeira.

Expressão Booleana é toda expressão onde o resultado é verdeiro ou falso.

Exemplo: 

num = 5

num < 5

ATENÇÃO!!!!!

Obs: em um loop while, é importante que cuidemos do critério de parada para não causar 
um loop infinito.

Exemplo 1:

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

Exemplo 2:

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')

# C ou Java

while(espressão){
    //execução do loop
}

#do while --> não existe em Python essa expressão.

do {
    //execução do loop
}while(expressão);
'''

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')







