# Fazer uma função que pergunta ao usuário se ele quer sair
# Fazer um while
# Executar a função dentro do while

def opcao() -> bool:

    escolha: str = input("Se quiser sair digite s: ")

    if escolha == "s":
        return True
    else:
        pass #Só passa sem dar erro

# fazer uma função para solicitar nome, cpf, peso, altura
# calcular imc
# retornar dados como dicionário

def pessoa() -> dict:
    
    nome: str = str(input("Qual seu nome? "))
    cpf: int = int(input("Qual seu cpf? "))
    peso: float = float(input("Qual seu peso? "))
    altura: float = float(input("Qual seu altura? "))
    imc: float = peso / (altura**2)

    usuario = {
        "nome": nome,
        "CPF": cpf,
        "peso": peso,
        "altura": altura,
        "IMC": imc
    }

    return usuario

while True:

   valor: str = opcao()
   if valor:
      break
        
        
