'''Crie um programa que solicite ao usuário uma lista de números inteiros e uma string
de mesmo comprimento. O programa deve substituir os números nos índices ímpares

da lista por caracteres correspondentes da string nos mesmos índices. Exiba a se-
quência resultante, separada por um espaço em branco. Exemplo:'''


caracteres = input('Digite uma sequencia de caracteres: ')
lista_string = list(caracteres)
lista_mesclada = []


for i in range(len(lista_string)):
    numeros_int = int(input('Digite numeros inteiros (De mesmo comprimento da sequencia de caracteres acima):'))
    if numeros_int % 2 != 0:
        lista_mesclada+=lista_string[i]
    else:
        lista_mesclada += str(numeros_int)
        
print(lista_mesclada)

