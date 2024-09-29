"""9.Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a
temperatura em graus Celsius.
C = (5 * (F-32) / 9). """

grausCelsios = 0
grausFare = float(input("Digite o grau em Farenheit: "))

grausCelsios = (5 * (grausFare - 32))/9

print(f"{grausFare}° Farenheit é o que Corresponde a {grausCelsios:.2f}° Celsios.") 
