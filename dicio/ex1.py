#nome é uma chave
nome : str = input("Informe seu nome: ")

# dicionário é um tipo de objeto
usuario: dict = {
    "nome": nome,
    "idade": 19,
    "matricula": 123456,
    "altura": 1.98,
    "endereco": {
        "rua": "Primeiro de Janeiro",
        "numero": 10,
        "cidade": "Belo Jardim",
        'estado': "PE"
    }
}

print(usuario)
print(usuario["matricula"])
print(usuario.get("idade"))

usuario["nome"] = "Maria"
usuario["peso"] = 77
print(usuario)

print(usuario["endereco"]["cidade"])
usuario["endereco"]["CEP"] = '551550-561'

del usuario["matricula"]

if "peso" in usuario and "altura" in usuario:
    print('Tem peso e Altura')
else:
    print('Falta coisa')

print(usuario)

for chave in usuario:
    print(usuario[chave])

for chave, valor in usuario.items():
    print(f"A chave é {chave} e o valor é {valor}.")

