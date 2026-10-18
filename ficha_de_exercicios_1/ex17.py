# 17. Escreva um programa que leia três lados de um quadrado
# e primeiro verifique se eles formam um triângulo válido (a soma de quaisquer dois lados deve ser maior que o terceiro); se válido, classifique-o também quanto ao tipo (equilátero, isósceles ou escaleno).

l1: float = float(input("Digite o lado 1: "))
l2: float = float(input("Digite o lado 2: "))
l3: float = float(input("Digite o lado 3: "))

if (l1 + l2) <= l3:
    print("Seu triângulo é inválido.")
else:
    print("Seu triângulo é válido.")
    if l1 != l2 and l1 != l3 and l3 != l2:
        print("Seu triângulo é escaleno.")
    elif l1 == l2 == l3:
        print("Seu triângulo é equilátero.")
    else:
        print("Seu triângulo é isócelaes.")
