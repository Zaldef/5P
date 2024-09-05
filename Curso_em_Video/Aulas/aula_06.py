"""
Este é o arquivo da Aula 06, tipos primitivos e saída de dados.

"""
# Tipos primitivos
int # Números inteiros, exemplo: 7, -4, 0, 9875
float # Números reais, exemplo: 4.5, 0.076, -15.223, 7.0
bool # Valores lógicos ou booleanos, exemplo: True, False
str # Textos, exemplo: 'Olá', '7.5', ''

# # Saída de dados
# # input sempre retorna uma string
# n1 = input('Digite um número: ')
# print(type(n1)) # type() retorna o tipo da variável
# n1 = int(n1)
# print(type(n1))

# # Exemplo de soma de dois números inteiros
# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))
# print(f'A soma entre {n1} e {n2} é {n1 + n2}') # Método f-string

# # Exemplo de booleano
# n1 = bool(input('Digite um número: '))
# print(n1) # Qualquer valor diferente de NULL é True

# Desafio 004
n = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(n))
print('É alfabético?', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('É um codigo ASCII?', n.isascii())
print('É um número decimal?', n.isdecimal())
print('É um digito?', n.isdigit())
print('É um identificador?', n.isidentifier())
print('Está em minúsculas?', n.islower())
print('É um número?', n.isnumeric())
print('É printavél?', n.isprintable())
print('Só tem espaços?', n.isspace())
print('Está capitalizada?', n.istitle())
print('Está em maiúsculas?', n.isupper())
