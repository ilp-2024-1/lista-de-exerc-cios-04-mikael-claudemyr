'''Para tanto, o programa deverá inicialmente solicitar ao usuário quantos valores serão
fornecidos para análise e só depois solicitar os valores a serem analisados. A análise
consistirá em identificar e apresentar a partir da sequência de valores fornecidos, o
menor valor, o maior valor e a média aritmética dos valores. Exemplos:'''

qtd_valores = int(input('Digite a quantidade de valores que serão imputados: '))
menor_valor = 'd'
maior_valor = 'c'
for i in range(qtd_valores):
    valores_analise = int(input('Digite valores para serem analisados: '))
    if menor_valor == 'd':
        menor_valor = valores_analise
    if maior_valor == 'c':
        maior_valor = valores_analise
    if valores_analise < menor_valor:
        menor_valor = valores_analise
    if valores_analise > maior_valor:
        maior_valor = valores_analise
    
print(menor_valor)
print(maior_valor)
        

