"""4.Faça um Programa que peça as 4 notas bimestrais e mostre a média. """

media = 0
total =0
for i in range(4):
    numero = float(input(f"Digite a {1+i}° Nota:"))
    total += numero

media = total/4

print(f"A media da nota foi: {media:.2f}")