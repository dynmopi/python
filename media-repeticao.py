# 06

print("Digite as duas notas das avaliações: ")

nota1 = int(input("Nota 1: "))

while nota1 < 0 or nota1 > 10:
    nota1 = int(input("Nota 1: "))

nota2 = int(input("Nota 2: "))

while nota2 < 0 or nota2 > 10:    
    nota2 = int(input("Nota 2:"))  

media = (nota1 + nota2)/2
print(f"A media das notas é de: {media}")