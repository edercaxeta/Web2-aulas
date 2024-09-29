"""     Faça um programa que recebe o salário de um colaborador e o reajuste segundo
o seguinte critério, baseado no salário atual:

● salários até R$ 280,00 (incluindo) : aumento de 20%
● salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
● salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
● salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser
realizado,
● Inflação do período: 3,8%

informe na tela:

1. o salário antes do reajuste;
2. o percentual de aumento aplicado;
3. o valor do aumento;
4. o novo salário, após o aumento;
5. o valor do aumento real, descontado a inflação;"""


while True:
    print("============Cauculo de Salario================")
    salario=float(input("Digite se salário: "))
    print(f"o salário antes do reajuste é: {salario}")

    soma=0
    percentual=0
    aumentoReal =0 

    if salario<=280.00:
        percentual = 20
        print(f"Seu percentual de Aumento é de 20%")
    elif salario <= 700.00:
        percentual = 15
        print(f"Seu percentual de Aumento é de 15%")
    elif salario <= 1500:
        percentual = 10
        print(f"Seu percentual de Aumento é de 10%")
    else:
        percentual = 5
        print(f"Seu percentual de Aumento é de 5%")


    soma = salario + salario*(percentual/100)
    aumentoReal = soma - (soma*3.8/100)
    print(f"O valor do aumeto foi de: R$ {percentual:.2f}")
    print(f"o novo salário, após o aumento é: {soma:.2f}")
    print(f"o valor do aumento real, descontado a inflação é: {aumentoReal:.2f}")
    print("=================================================")

    resposta = input("Deseja calcular outro salário? (s/n): ").lower()

    if resposta != 's':
        print("Encerrando o programa.")
        break