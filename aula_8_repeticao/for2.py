""" Escreva um algoritmo que converta
uma temperatura de graus
Fahrenheit para graus Celsius, sendo
que:
– A fórmula de conversão é:
   c= (5*(f-32))/9 

– A saída deve listar a conversão das
temperaturas de 50 a 150 graus F, de
10 em 10 graus. """

""" fahrenheit = list(range(50, 151, 10)) pode ser assim também """
fahrenheit =[]
for i in range(50,151,10 ):
    fahrenheit.append(i)

print(fahrenheit)

for f in fahrenheit:
    celsios = (5*(f-32))/9
    print(f"{f}°Fahrenheit é igual a {celsios:.2f}° Celsius")