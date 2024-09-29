maior = 0
for i in range(3):
    num = int(input(f"Digite {i+1}° numero: "))
    if num > maior:
        maior = num

print(f"o maior foi: {maior}")    
''' ========================================================== '''

num1 = int(input(f"Digite 1° numero: "))
num2 = int(input(f"Digite 2° numero: "))
num3 = int(input(f"Digite 3° numero: "))

if num1 > num2 and num2 > num3:
    maior = num1
elif num2 > num3:
    maior = num2
else:
    maior = num3
    
print(f"o segundo maio é: {maior}")