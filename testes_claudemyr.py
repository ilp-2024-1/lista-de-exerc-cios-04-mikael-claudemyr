# 1. Escreva um programa que leia 10 valores inteiros e armazene em uma lista. O pro-
# grama deve imprimir no terminal quantos valores pares foram digitados pelo usuário.

# Dica: use o operador “%” para verificar se o número é par (ZERO é neutro, ZERO NÃO
# É PAR). Exemplos:

# lista=[]
# quant=0
# for x in range(10):
#     lista.append(int(input('Valor {}: '.format(x+1))))
# for xx in lista:
#     if xx %2 ==0 and xx !=0:
#             quant+=1               
# print(f'Quantidade de números pares é: {quant}')

# 3. leia 10 valores inteiros e armazene em uma lista. O programa deve imprimir no terminal
# quantos valores pares foram digitados pelo usuário. Dica: use o operador “%” para
# verificar se o número é par (ZERO é neutro, ZERO NÃO É PAR). Exemplos:

# lista=[]
# quant=0
# for x in range(10):
#     lista.append(int(input('Valor {}: '.format(x+1))))
# for xx in lista:
#     if xx %2 ==0 and xx !=0:
#             quant+=1               
# print(f'Quantidade de números pares é: {quant}')

# 4. Escreva um programa que receba como entrada 3 parâmetros: um valor inteiro corres-
# pondente à quantidade de elementos de dois arrays unidimensionais; duas sequências
# de valores do tamanho do primeiro parâmetro, os quais deverão ser armazenados em
# duas listas distintas. Em seguida, o programa deverá criar uma lista resultante formada
# pela intercalação dos valores de cada uma das sequências de entrada. Como saída o
# programa deverá imprimir as duas listas iniciais e a lista resultante. Exemplo:


# quantidade_elementos=3
# lista1=[]
# lista2=[]
# lista3=[]

# for x in range(quantidade_elementos):
#     lista1.append(input('{}º da lista 1: '.format(x+1))) 

# for x in range(quantidade_elementos):
#     lista2.append(input('{}º da lista 2: '.format(x+1))) 

# for i in range(len(lista1)):
#     lista3.append(lista1[i])
#     lista3.append(lista2[i])

# print(f'Ver resultado 1 : lista 1: {lista1} lista2: {lista2} lista 3(intercalada): {lista3}')

# 5  Escreva um programa que receba como entrada uma sequência de valores inteiros.
# Para tanto, o programa deverá inicialmente solicitar ao usuário quantos valores serão
# fornecidos para análise e só depois solicitar os valores a serem analisados. A análise
# consistirá em identificar e apresentar a partir da sequência de valores fornecidos, o
# menor valor, o maior valor e a média aritmética dos valores. Exemplos:


# listaOrdenada=[]
# listaSemOrdem=[]

# n=int(input('Forneça a quantidade de valores inteiros: '))
# total=2
# # aqui fizemos a ordenação para saber qual é o menor e maior número
# for x in range(n):
#     n = int(input('Digite o {}º valor: '.format(x+1)))
#     listaSemOrdem.append(n)
#     incluido = False
#     for i in range(len(listaOrdenada)):
#         if n<listaOrdenada[i] :
#             listaOrdenada.insert(i, n)
#             incluido = True
#             break

#     if not incluido:
#         listaOrdenada.append(n)

# # aqui eu somo e divido pela quantidade de numeros para chegar na média
# vr=0
# media=0
# for y in range(len(listaOrdenada)):
#     vr+=listaOrdenada[y]
# media=vr/len(listaOrdenada)

# print(f' O Menor número é: {listaOrdenada[0]} , O maior é: {listaOrdenada[-1]} a média é : {media: ,.2f}')


# 8. Escreva um programa que receba como entrada uma string constituída por uma se-
# quência de números inteiros separados por espaço. O programa deverá transformar

# essa string em uma lista de números inteiros e apresentar o resultado da soma dos
# valores das posições ímpares dessa lista. Exemplos:

# strSequencia= '25 44 65 22 88 35 98 10 55 23 633 5 87 55'
# Nlista= []
# total=0

# Nlista=strSequencia.split()

# for x in range(len(Nlista)):
#     if x %2 != 0:
#         total+=int(Nlista[x])
# print(total)