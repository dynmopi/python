n = int(input("Quantos valores serão lidos? "))

# 03
# for i in range(n):
#     print(i)

i = 1
soma = 0
while i <= n :
    valor = int(input(f"V{i}: "))
    i = i + 1
    soma = soma + valor

media = soma / n
print(f"Media: {media}")

    