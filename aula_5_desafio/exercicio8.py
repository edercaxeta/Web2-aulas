""" 8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês. """


salario= 0

horas = float(input("Quanto Você ganha por hora? "))
numeroHora = float(input("Quantas Horas Você Trabalha por Mês? "))

salario = horas * numeroHora

print(f"O Seu Salario Esse Mês foi: {salario:.2f} ")


