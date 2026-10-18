# 15. Escreva um programa que leia um número
#  e verifique se ele está dentro do intervalo entre 10 e 50 (inclusive), usando um único operador lógico and

numero: float = float(input("Digite um número: "))

if numero >= 10 and numero <= 50:
    print("Você digitou um número entre 10 e 50.")
else:
    print('Você não digitou um número entre 10 e 50.')