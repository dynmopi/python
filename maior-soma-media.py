# 08

# Entrar via teclado com dez valores positivos. Consistir a digitacao e
# enviar mensagem de erro, se necessario. Apos a digitacao, exibir:
# A. O maior valor;
# B. A soma dos valores;
# C. A media aritmetica dos valores.

maior = 0
i = 0
soma = 0
for c in range(10):
    i += 1
    n = int(input(f"Digite o {i}ª valor: "))

    soma = soma + n
    if n > maior:
        maior = n

media = soma / 10
print("A soma é igual a ", soma)
print("A média é igual a ", media)
print("O maior número a ", maior)

