'''
Recebendo dados do usuário

input -> Todo ddo recebido via input é do tipo String.

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos: 

- aspas simples: 'Angelina Jolie'
- aspas duplas: "Angelina Jolie"
- aspas simples triplas: são as mesmas aspas simples dos comentários
- aspas duplas triplas: """Angelina Jolie"""

'''
# Entrada de dados
# print("Qual é o seu nome? ")
# nome = input()

nome = input("Qual o seu nome? ")

# Exemplo de print antigo 2.x
# print("Seja bem vindo(a) %s" % nome)

# Exemplo de print moderno 3.x
# print("Seja bem vindo(a) {0}".format (nome))

# Exemplo de print mais atual
print(f"Seja bem vindo(a) {nome}")


# print("Qual a sua idade? ")
# idade = input()

idade = input("Qual a sua idade? ")

#processamento

# Saída de dados
# Exemplo de print antigo 2.x
# print("O(A) %s tem %s anos" % (nome, idade))

# Exemplo de print moderno 3.x
#print("O(A) {0} tem {1} anos".format (nome, idade))

# Exemplo de print mais atual
print(f"O(A) {nome} tem {idade} anos")

'''
int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro. 

'''
print(f"O(A) {nome} nasceu em {2022 -  int(idade)}") 
