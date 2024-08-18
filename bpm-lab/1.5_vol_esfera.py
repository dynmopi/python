# 1.5 Volume da Esfera
# Calcular e exibir o volume de uma esfera a partir do valor de seu
# diâmetro que será digitado.
import math
# v = 4/3 pi r^3
# diametro = 2.r

pi = 3.14

print("Cálculo do volume de um esfera a partir do valor de seu diâmetro")
diametro = float(input("Digite o valor do diâmetro: "))

raio = diametro/2
volume = (4*pi*math.pow(raio, 3))/3

print("O volume a partir do diâmetro", diametro, "é de:", volume)


