'''
Escopo de variáveis

1 - Variáveis globais: são reconhecidas, ou seja, seu escopo compreende todo o programa;

2 - Variáveis locais: são reconhecidas apenas localmente onde foram declaradas, ou seja, 
seu escopo está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos: 

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável,
nós não colocamos o tipo de dados dela. Este tipo é inferido automaticamente ao atribuirmos
o valor da variável.

'''

numero = 42 # Exemplo de variável global.
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

numero = 42

if numero > 10:
    novo = numero + 10 # A variável novo está declarada localmente no bloco de if. 
    print(novo)