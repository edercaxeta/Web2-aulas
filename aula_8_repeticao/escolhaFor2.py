""" Altere o programa que exibe o menu de operações matemáticas para que ele se
comporte da seguinte forma: – Leia dois números inteiros do usuário;
– Exiba um menu com as opções: 
    • Somar estes dois números; 
    • Subtrair estes dois números; 
    • Multiplicar estes dois números; 
    • Voltar para a janela de leitura dos números;

– O algoritmo deve executar a opção escolhida, exibir o resultado e reapresentar o menu. """

print("\n\n=====================================Escolha a operação=================================")


while True:
    print("\n=======================================================================")    
    print("|Digite 1 para Somar estes dois números                               |")
    print("|Digite 2 para Subtrair estes dois números                            |")
    print("|Digite 3 para Multiplicar estes dois números                         |")
    print("|Digite outro valor para Voltar para a janela de leitura dos números  |")
    print("=======================================================================\n") 
    escolha = int(input("Escolha: "))
    
    
    if escolha in[1,2,3]:
        numeros=[]
        for i in range(2):
            num = int(input(f"Digite o {i+1}° numero: "))
            numeros.append(num)
        
        if escolha== 1:
            resposta= numeros[0] + numeros[1]
        elif escolha== 2:
            resposta= numeros[0] - numeros[1]
        elif escolha== 3:
            resposta= numeros[0] * numeros[1]
        
        print(f"A resposta é: {resposta}")
        
        resposta = input("Deseja realizar outra operação? (s/n): ").lower()

        if resposta != 's':
            print("Encerrando o programa.")
            break
    else:
        print("Voltando para a janela de leitura dos números.")
        continue