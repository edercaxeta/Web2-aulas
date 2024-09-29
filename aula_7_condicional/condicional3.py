numero=[]
resultado = 0
for i in range(2):
    num = int(input(f"Digite {i+1}° numero: "))
    numero.append(num)
        
print("Digite 1 para somar os dos numeros")    
print("Digite 2 para subrair os dois numeros")    
print("Digite 3 para multiplicar os dois numeros")    
escolha = int(input("Escolha: "))
        
if escolha == 1:
    resultado = numero[0] + numero[1]
    print(f"A soma de {numero[0]} e {numero[1]} é: {resultado}") 
elif escolha == 2:
    resultado = numero[0] - numero[1] 
    print(f"A subtração de {numero[0]} e {numero[1]} é: {resultado}") 
elif escolha == 3:
    resultado = numero[0] * numero[1] 
    print(f"A multiplicação de {numero[0]} e {numero[1]} é: {resultado}") 
else:
    print("erro")   