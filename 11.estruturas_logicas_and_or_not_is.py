'''
Estruturas Lógicas: and, or, not, is.

Operadores unários: 
    -not, is.
Operadores binários: 
    - and, or

Regras de funcionamento:

Para o and ambos os valores pecisam serem verdadeiros (True)
Para o 'or', um ou outro valor precisa ser verdadeiro (True)
ara o 'not', o valor do boolenao é invertido, ou seja, se for True vira False, se for 
False vira True
'''
# and
ativo = True
logado = True

if ativo and logado:
    print('Bem vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque o seu e-mail!')

# or
ativo = False
logado = True

if ativo or logado:
    print('Bem vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque o seu e-mail!')

# not
ativo = True
logado = False
# Se não estiver ativo faça isto:
if not ativo:
    print('Bem vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque o seu e-mail!')

# ativo é falso?
print(ativo is False)