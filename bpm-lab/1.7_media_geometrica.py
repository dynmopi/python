import math
# Calcular e exibir a média geométrica de dois valores quaisquer que
# serão digitados.

# pow(x1*x2*xn, 1/n)

print("Cálculo de média geométrica de dois valores")
valor1 = int(input("Digite o valor 1: "))
valor2 = int(input("Digite o valor 2: "))

media = math.sqrt(valor1*valor2)

print("A media de", valor1, "e", valor2, "é de", media)


