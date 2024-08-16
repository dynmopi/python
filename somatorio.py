# 07

# A partir de um numero inteiro
# positivo e menor que 21, exibir a
# soma dos numeros inteiros de 1 ate o
# numero informado.

print("Soma de N elementos\n\n")

# while n < 1 or n >= 21:
# estrutura do while

while True:
    n = int(input("Insira um numero entre 1 e 20: "))
    if n >= 1 and n < 21:
        break
    print("[ERRO] Digite o número pedido")

soma = 0

for n in range(n): # por padrao, o n comeca em 0
    n += 1
    soma = soma + n
    
print(f"A soma dos valores consecutivos até o número {n} é de: {soma}")
