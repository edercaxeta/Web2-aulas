""" Escreva um algoritmo que calcule
o valor de S, segundo a fórmula
abaixo:
    s= 1/1- 2/4 + 3/9 - 4/16 + 5/15 - 6/36 +... 10/100 """

cont = 1
calculaS = 0

while cont <= 10:
    if cont % 2 == 0: #impa subtrai
        calculaS -= cont / (cont ** 2)
    else: #par soma
        calculaS += cont / (cont ** 2)
    cont += 1
    
print(f"O valor de S é: {calculaS:.4f}")