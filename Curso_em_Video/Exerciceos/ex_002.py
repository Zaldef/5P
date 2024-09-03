"""
Este é o segundo exercício do curso de Python do Curso em Vídeo.
"""
# Crie um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
nome = input('Qual é o seu nome?')
print('Seja bem vindo', nome,'!, fique a vontade') # Concatenação com vírgula
print('Seja bem vindo '+ nome + ' !, fique a vontade') # Concatenação com +

print('Seja bem vindo {} !, fique a vontade'.format(nome)) # Método format 
print(f'Seja bem vindo {nome} !, fique a vontade') # Método f-string

print('Seja bem vindo', nome,'!, fique a vontade', sep=' ') # Concatenação com vírgula e separador
print('Seja bem vindo '+ nome + ' !, fique a vontade', sep=' ') # Concatenação com + e separador
print('Seja bem vindo {} !, fique a vontade'.format(nome), sep=' ') # Método format e separador
