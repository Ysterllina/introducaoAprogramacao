# 16. Escreva um programa que leia a renda mensal,
#  a idade 
# e se a pessoa possui restrição no nome ( True / False ), e informe se ela pode solicitar um cartão de crédito (regra: renda ≥ R$1.500 e idade ≥ 18 e não possuir restrição).

renda_mensal: float = float(input("Qual a sua renda mensal? "))
idade: int = int(input("Qual a sua idade? "))

if renda_mensal >= 1500 and idade >= 18:
    print("Você pode solicitar cartão de crédito.")
else:
    print("Você não pode solicitar cartão de crédito.")
    