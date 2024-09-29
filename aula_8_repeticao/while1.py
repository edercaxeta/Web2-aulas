""" Escreva um algoritmo que:
– Receba um número inteiro
maior que zero;
– Calcule o fatorial deste
número:
• 0! = 1
• n! = n*(n-1)*(n-2)*...*1 """

valor = int(input("Digite o numero que quer calcular o Fatorial: "))
contador = 1
fatorial = 1
while contador <= valor:
    fatorial = fatorial*contador
    contador += 1
    
print(f"O fatorial de {valor} é: {fatorial}")