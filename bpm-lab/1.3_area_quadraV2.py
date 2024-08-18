# Calcular e exibir a área de um quadrado a partir do valor de sua
# diagonal que será digitado.

    #     // diagonal == l * sqrt(2)
    #     // l == diagonal / sqrt(2)
    #     // l^2 == diagonal^2 / 2
    #     // area == l^2

print("Cálculo da área de um quadrado a partir da diagonal")
diagonal = float(input("Digite o valor da diagonal: "))

lado_Quadrado = pow(diagonal, 2) / 2
area_do_Quadrado = lado_Quadrado

print("O valor da área do quadrado é de:", area_do_Quadrado)