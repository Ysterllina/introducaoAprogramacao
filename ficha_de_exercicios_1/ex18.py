# 18. Escreva um programa que simule a emissão de uma carteira de motorista: o candidato só pode emitir se tiver 18 anos ou mais, não possuir CNH suspensa e ter sido aprovado no exame (nota ≥ 7). Leia essas informações e informe se a emissão foi autorizada, indicando o motivo caso não seja.

idade: int = int(input("Qual sua idade? "))
nota: float = float(input("Qual sua nota no exame? "))
cnh_suspensa: int = int(input("Sua CNH está suspensa? Responda Sim ou Não. "))

if idade >= 18 and nota >= 7 and cnh_suspensa == "Não":
    print("Você pode emitir carteira de motorista.")
