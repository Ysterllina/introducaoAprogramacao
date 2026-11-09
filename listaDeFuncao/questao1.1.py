# Questão 1.1 --- Implementação da função

# Implemente a função tamanho(texto) 
# que recebe uma string e retorna a quantidade de caracteres

# existentes nela.
# O cálculo deve ser sem utilizar a função len() .
# Considere que espaços em branco também devem ser contabilizados.

# texto tem varias letras
# pegar cada caractere de texto e contar
# armazenar a quantidade de caracteres em uma variável
# restornar a variável

texto = "bom dia"
def tamanho(texto: str) -> int:
    contador = 0
    for _ in texto:
        contador +=1
    return contador

print(tamanho(texto))