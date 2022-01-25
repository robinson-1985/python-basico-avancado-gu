'''
Estruturas condicionais
if, else, elif

'''

idade = 15
if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos de idade')
elif idade == 26:
    print('Tem 26 anos de idade')
else:
    print('Maior de idade')

'''
Existe outra forma de fazer o esquema acima, mas, não é aconselhado. 

if idade < 18:
    print('Menor de idade')

if idade == 18:
    print('Tem 18 anos de idade')

if idade == 26:
    print('Tem 26 anos de idade')

if idade == 18:
    print('Maior de idade')

'''