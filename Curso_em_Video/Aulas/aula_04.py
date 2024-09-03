# #colocar entre '' define uma string
# print('Olá, Mundo!')
# #escrita de números, usando o + ele irá juntar as strings
# print('7' + '4')
# print('7', '4')
# #para somar números, não se deve colocar entre ''
# print(7+4)
# #para juntar string com número, deve-se usar a vírgula
# # print('olá'+ 5) #não funciona
# print('olá',5)
# #para pular linha, usa-se \n
# print('Olá\nMundo!')
# #para usar aspas, deve-se usar \'
# print('Olá, \'Mundo\'!')


# #Variáveis
# nome = 'Gui'
# idade = 20
# peso = 92.4

# print(nome, idade, peso) # sem separador
# print(nome, idade, peso, sep=', ') # sep = separador de argumentos\
# print(nome, idade, peso, sep=' - ', end='!\n') # end = final do print

# nome = input('Qual é o seu nome? ') #input sempre retorna uma string
# idade = input('Quantos anos você tem? ') #input sempre retorna uma string
# peso = input('Qual é o seu peso? ') 
# print(nome, idade, peso)

# Desafio 01
name = input('Qual é o seu nome? ')
print('Olá', name, '! Prazer em te conhecer!')	
# Desafio 02
dia = input('Qual é o dia do seu nascimento? ')
mes = input('Qual é o mês do seu nascimento? ')
ano = input('Qual é o ano do seu nascimento? ')
print('Você nasceu no dia', dia, 'de', mes, 'de', ano, '. Correto?')
# Desafio 03
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = num1 + num2
print('A soma entre', num1, 'e', num2, 'é', soma)
