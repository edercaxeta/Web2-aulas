""" Escreva um algoritmo que:
– Receba um número inteiro
maior que zero;
– Calcule o fatorial deste
número:
• 0! = 1
• n! = n*(n-1)*(n-2)*...*1 """

valor = int(input("Digite o numero que quer caucular o Fatorial: "))
fatorial= 1
for i in range(1,valor+1):
    fatorial = fatorial*i
print(f"O fatorial de {valor} é: {fatorial}")