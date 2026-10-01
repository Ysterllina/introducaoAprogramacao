# matriz é um vetor de vetores, ou seja, uma lista de listas

#vetor
vetor:list[int] = [3, 2, 1]

#matriz
matriz: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz)
print(matriz[0])
print(matriz[0][0])

matriz[0][0] = 0
print(matriz)

# exemplo de tabuada
#for i in range(1, 10):
#    for j in range(1, 10):



