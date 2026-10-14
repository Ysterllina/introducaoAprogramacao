def dividir(x:int, y:int) -> int:
    if y != 0:
        conta: int = x // y
        return conta
    else:
        print("Impossível dividir por 0")

print(dividir(8, 0))