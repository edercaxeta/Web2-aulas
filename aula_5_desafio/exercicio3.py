""" num1 = int(input("Digite o primeiro Numero: "))
num2 = int(input("Digite o segundo Numero: "))

soma = num1 +  num2

print(f"O valor da soma foi: {soma}") """
""" ================================================================================================ """

"""3.Faça um Programa que peça dois números e imprima a soma. """
soma = 0
for i in range(2):
  numero = int(input(f"Digite o {1+i}° numero: "))
  soma += numero

print(f"O valor da soma foi: {soma}")
