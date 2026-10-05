from random import randint

# _ quando não vai usar a variável
bombs = []
for i in range(9):
    x, y = [randint(0,4) for _ in range(2)]
    bombs.append((x,y))

bomba = "💣"
agua = "💧"

tabuleiro = [
     #0,      1,     2,    3,    4
    ["🟦", "🟦", "🟦", "🟦", "🟦"], #0
    ["🟦", "🟦", "🟦", "🟦", "🟦"], #1
    ["🟦", "🟦", "🟦", "🟦", "🟦"], #2
    ["🟦", "🟦", "🟦", "🟦", "🟦"], #3
    ["🟦", "🟦", "🟦", "🟦", "🟦"]  #4
]

while True:
    opcao:str = str(input("QUER CONTINUAR? (S ou N)"))
    if opcao == "N":
        break
    else:
       x: int = int(input("Digite a coordenada x: "))
       y: int = int(input("Digite a coordenada y: "))

       if (x, y) in bombs:
           print()
           # Coloca bomba substituindo o quadrado azul na posição (x, y)

