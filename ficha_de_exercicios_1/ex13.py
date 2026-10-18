# 13. Escreva um programa que leia a idade de uma pessoa 
# e informe sua situação eleitoral: menor de 16 (não vota), 16 ou 17 (voto facultativo), 18 a 70 (voto obrigatório), acima de 70 (voto facultativo).

idade: int = int(input("Qual a sua idade? "))

if idade < 0:
    print("Digite uma idade válida.")
elif idade < 16:
    print("Você não vota.")
elif idade < 18:
    print("Voto facultativo.")
elif idade < 70:
    print("Voto obrigatório.")
else:
    print("Voto facultativo.")
