""" Escreva um algoritmo que imprima todos os resultados
possíveis da combinação de dois dados de 6 lados;
– Ex: (1,1), (6,6), (2,5), (5,2). """

for dado1 in range(1, 7):
    for dado2 in range(1, 7):
        print(f"({dado1}, {dado2})")