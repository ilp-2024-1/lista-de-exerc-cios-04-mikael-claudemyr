# Escreva um programa que recebe como entrada valores inteiros para criar duas listas

# de mesmo tamanho. O tamanho das listas deverá ser definido pelo usuário. O pro-
# grama deverá somar os valores pares e ímpar de cada uma das listas. Em seguida,

# comparar as somas e informar qual dos somatórios é maior ou se há um empate.
# Exemplos:

tam_lista = int(input('Digite a qtd de itens da lista: '))
lista_valores_1 = []
lista_valores_2 = []
soma_numeros_pares_lista1 = 0
soma_numeros_impares_lista1 = 0
soma_numeros_pares_lista2 = 0
soma_numeros_impares_lista2 = 0

#lista 1
for i in range(tam_lista):
    lista_1 = int(input('Digite valores para armarenar na lista 01: '))
    lista_valores_1 += [lista_1]
    if lista_1 % 2 == 0:
        soma_numeros_pares_lista1 += lista_1
    else:
        soma_numeros_impares_lista1 +=lista_1
        
# lista 2
for j in range(tam_lista):
    lista_2 = int(input('Digite valores para armarenar na lista 02: '))
    lista_valores_2 += [lista_2]
    if lista_2 % 2 == 0:
        soma_numeros_pares_lista2 += lista_2
    else:
        soma_numeros_impares_lista2 +=lista_2

print(f'\nA soma dos numeros da lista 1, que são pares: {soma_numeros_pares_lista1}. A soma dos valores lista 1 que são impares são: {soma_numeros_impares_lista1}')
print(f'\nA soma dos numeros da lista 2, que são pares: {soma_numeros_pares_lista2}. A soma dos valores lista 2 que são impares são: {soma_numeros_impares_lista2}')


# verificando qual lista tem maior soma de par
if soma_numeros_pares_lista1 > soma_numeros_pares_lista2:
    print(f'\nA soma dos pares da lista 1 é maior. A soma dos numeros pares da lista 1 é: {soma_numeros_pares_lista1}, já a soma dos numeros pares da lista 2: {soma_numeros_pares_lista2}.')
elif soma_numeros_pares_lista1 < soma_numeros_pares_lista2:
        print(f'\nA soma dos pares da lista 2 é maior. A soma dos numeros pares da lista 1 é: {soma_numeros_pares_lista1}, já a soma dos numeros pares da lista 2: {soma_numeros_pares_lista2}.')
elif soma_numeros_pares_lista1 == soma_numeros_pares_lista2:
     print(f'\nOra Ora Ora... temos um empate. Soma pares lista 1 equivale: {soma_numeros_pares_lista1} e a soma dos pares lista 2 equivale: {soma_numeros_pares_lista2}.')


# verificando qual lista tem maior soma de impar
if soma_numeros_impares_lista1 > soma_numeros_impares_lista2:
    print(f'\nA soma dos impares da lista 1 é maior. A soma dos numeros impares da lista 1 é: {soma_numeros_impares_lista1}, já a soma dos numeros impares da lista 2: {soma_numeros_impares_lista2}.')
elif soma_numeros_pares_lista1 < soma_numeros_pares_lista2:
        print(f'\nA soma dos impares da lista 2 é maior. A soma dos numeros impares da lista 1 é: {soma_numeros_pares_lista1}, já a soma dos numeros impares da lista 2: {soma_numeros_impares_lista2}. Logo, a soma dos pares da lista 2 é maior.')
elif soma_numeros_impares_lista1 == soma_numeros_impares_lista2:
     print(f'\nOra Ora Ora... temos um empate. Soma impares lista 1 equivale: {soma_numeros_pares_lista1} e a soma dos impares lista 2 equivale: {soma_numeros_pares_lista2}.')