# 14. Escreva um programa que leia o salário de um funcionário
# e aplique reajuste por faixa: até R$1.500 → 10%; 
# de R$1.500 a R$3.000 → 7%; acima de R$3.000 → 5%. Imprima o novo salário.

salario_base: float = float(input("Funcionário, qual é o seu salário mensal? "))

if salario_base < 0:
    print("Digite um salário válido.")
elif salario_base < 1500:
    print(f"Seu salário teve um reajuste e agora é R$: {salario_base * 1.1}")
elif salario_base < 3000:
    print(f"Seu salário teve um reajuste e agora é R$: {salario_base * 1.07}")
else:
    print(f"Seu salário teve um reajuste e agora é R$: {salario_base * 1.05}")
