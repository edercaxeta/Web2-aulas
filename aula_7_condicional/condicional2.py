import math

numA = int(input(f"Digite a numero: "))
numB = int(input(f"Digite b numero: "))
numC = int(input(f"Digite c numero: "))

delta = 0
x1 = 0
x2 = 0

delta = numB*numB - 4*numA*numC
print(f"Delta é : {delta}")

if delta > 0:
    x1 = (-numB + math.sqrt(delta))/ 2*numA
    x2 = (-numB - math.sqrt(delta))/ 2*numA

elif delta == 0:
    x1 = x2 = -numB / 2*numA
else:
    print("Não existe raiz reais")
    
print(f"X1 é: {x1}")
print(f"X2 é: {x2}")