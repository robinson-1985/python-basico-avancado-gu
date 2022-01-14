'''
Tipo Bolleano

Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro;
False -> Falso.

Obs: Sempre com a inicial maiúscula.

Errado:

true, false.

Sempre: True or False.

'''

ativo = False
print(ativo)

'''
Operações básicas:

Negação (not): 

Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso o resultado será verdadeiro. Ou seja, sempre é o contrário.
'''

print(not ativo)

logado = False

'''
Outra negação é o Ou(or):

É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro:

True or True
True

True or False
True

False or True
True

False or False
False
'''

print(ativo or logado)

'''
E (and):

Também é uma operação binária , ou seja, depende de dois valores. Ambos os valores devem 
ser verdadeiros.

True and True -> True
True and False -> False
False and True -> False
False and False -> True
'''