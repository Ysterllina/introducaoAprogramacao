# fazer uma função para solicitar nome, cpf, peso, altura
# calcular imc
# retornar dados como dicionário

def pessoa() -> list[list]:

nome: str = str(input("Qual seu nome? "))
cpf: int = int(input("Qual seu cpf? "))
peso: float = float(input("Qual seu peso? "))
altura: float = float(input("Qual seu altura? "))

ser_humano