def ola(nome:str) -> None: #Nulo
    print(f"Olá {nome}!")

ola("Emily")
ola("Ana")

def ola(nome:str) -> str:
    return f"Olá {nome}"

print(ola("Mano"))