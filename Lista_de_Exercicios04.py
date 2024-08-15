# 1. Escreva um programa que leia 10 valores inteiros e armazene em uma lista. O pro-
# grama deve imprimir no terminal quantos valores pares foram digitados pelo usuário.

# Dica: use o operador “%” para verificar se o número é par (ZERO é neutro, ZERO NÃO
# É PAR). Exemplos:

lista=[]
quant=0
for x in range(10):
    lista.append(int(input('Valor {}: '.format(x+1))))
for xx in lista:
    if xx %2 ==0 and xx !=0:
            quant+=1               
print(f'Quantidade de números pares é: {quant}')