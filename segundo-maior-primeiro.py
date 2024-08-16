print("Programa de número segundo maior que primeiro: ")

# 04
# do while 

while True:
    primeiro = int(input("Digite um numero inteiro: "))  
    segundo = int(input(f"Digite um numero inteiro maior ou igual a {primeiro}: "))
    if segundo > primeiro:
        break
    print("[ERRO] Digite os números novamente")
print("Fim")