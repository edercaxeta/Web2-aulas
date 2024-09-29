""" Escreva um algoritmo que:
– Leia nomes e idades de uma quantidade indeterminada de pessoas;
– Calcule e imprima o nome e a idade da pessoa mais velha;
– Quando o usuário não quiser digitar mais pessoas, ele digitará a palavra "fim". """


print("===========================Mais Velha==============================")

pessoas = []

while True:
    nome = input("Digite Seu Nome: ")
    idade = int(input("Digite Sua Idade: "))
    
    pessoas.append({'nome': nome, 'idade': idade})
    
    maior_idade = 0
    for pessoa in pessoas:
        if pessoa['idade'] > maior_idade:
            maior_idade = pessoa['idade']
            pessoa_mais_velha = pessoa
    
    resposta = input("Deseja encerrar digite Fim, ou aperte qualquer tecla pra continuar ").lower()

    if resposta == 'fim':
        break
    
    
print(f"\nA pessoa mais velha é {pessoa_mais_velha['nome']} com {maior_idade} anos.")
