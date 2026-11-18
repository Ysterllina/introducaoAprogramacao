frase = input("Digite uma frase: ")

# def frase_ao_contrario(frase: str) -> str:

#      nova_frase = ""
#      for i in range(len(frase)-1, -1, -1):
#          nova_frase = nova_frase + frase[i]
#      return nova_frase

# print(frase_ao_contrario(frase))
 
# def palindromo(frase:str) -> str:
#     nova_frase = ""
#     for i in range(len(frase)-1, -1, -1):
#         nova_frase = nova_frase + frase[i]
#     if frase == nova_frase:
#         return print("Palindromo.")
#     else:
#         return print("Não é um palindromo.")

# palindromo(frase)

def cifra_de_cezar(frase) -> str:
    ALFABETO = "abcdefghijklmnopqrstuvwxyz"
    frase_cifrada = ""
    for i in frase:
        frase = (ALFABETO[i]+2)
        frase_cifrada = frase_cifrada + frase
    return frase_cifrada

print(cifra_de_cezar(frase))

# tem q andar a quatidade de casas
# frase exemplo