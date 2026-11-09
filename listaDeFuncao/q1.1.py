# Questão 1.1 --- Implementação da função
# Implemente a função tamanho(texto) , que recebe uma string e retorna a quantidade de caracteres
# existentes nela.
# O cálculo deve ser sem utilizar a função len() .
# Considere que espaços em branco também devem ser contabilizados.

def tamanho(texto: str) -> int:
    contador = 0
    for _ in texto:
        contador+=1
    return contador

# questão 2

print(
    tamanho("Olá mundo!")
    )


# questão 3