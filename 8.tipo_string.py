'''
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas;
- Estiver entre aspas simples duplas.

nome = 'Geek University'
print(nome)
print(type(nome))

- Atenção para o exemplo abaixo, tem que colocar aspas duplas:
nome = "Gina's Bar"
print(nome)
print(type(nome))



nome = 'Angelina \nJones'
print(nome)
print(type(nome))


nome = """Angelina
Jolie"""
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) - transforma em uma lista de strings.

nome = 'Geek University'
print(nome[0:14]) - imprime todas as letras (Slice de string)

print(nome.split()[0]) - slice de string

nome = 'Geek University'
print(nome[::-1]) - come do primeiro elemento, vá até o último elemento e inverta.

'''

nome = 'Geek University'
print(nome[::-1]) # Inversão da string em forma pythonica.

print(nome.replace('G', 'P')) # -> substitui uma letra por outra

print(type(nome))

texto = 'socorram me subino onibus em marrocos' #Palíndromo
print(texto)

print(texto[::-1])