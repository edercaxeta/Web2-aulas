"""7.Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área
para o usuário. """

area:0
dobro:0

lado = float(input("Digite um numero: "))

area = lado*lado
dobro= area*2

print(f"A area é: {area:.2f}")
print(f"o dobro da area é: {dobro:.2f}")