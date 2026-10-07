from random import randint

# _ quando não vai usar a variável
bombs = []
for i in range(9):
    x, y = [randint(0,4) for _ in range(2)]
    bombs.append((x,y))

bomba = "💣"
agua = "💧"

tabuleiro = [
     #0,     1,    2,     3,    4
    ["🟦", "🟦", "🟦", "🟦", "🟦"], #0
    ["🟦", "🟦", "🟦", "🟦", "🟦"], #1
    ["🟦", "🟦", "🟦", "🟦", "🟦"], #2
    ["🟦", "🟦", "🟦", "🟦", "🟦"], #3
    ["🟦", "🟦", "🟦", "🟦", "🟦"]  #4
]

jogada = 0
pontuacao = 0
coordenadas_usadas = [] 

while True:
    opcao:str = str(input("QUER CONTINUAR? (S ou N)"))
    if opcao == "N":
        break
    else: #linha imprime cada linha do TABULEIRO
       jogada = jogada + 1
    
       for linha in tabuleiro:
           print(linha)
       x: int = int(input("Digite a coordenada x: "))
       y: int = int(input("Digite a coordenada y: "))
       

       if (x, y) in coordenadas_usadas:
           print("Você já usou esta cordenada, tente novamente com uma coordenada ainda não utilizada.")
           

       else:
           coordenadas_usadas.append([x,y])
           if (x, y) in bombs:
                tabuleiro[x][y] = bomba
                pontuacao = pontuacao - 5
                print(f"Lamento, você acertou na bomba e perdeu 5 pontos!")
           else:
                tabuleiro[x][y] = agua
                pontuacao = pontuacao + 10
                print(f"Parabens você acertou na água e ganhou 10 pontos!")

           for linha in tabuleiro:
                print(linha)

       # Contar as jogadas do jogador
       print(f"Quantidade de jogadas: {jogada}")
       print(f"Você está com {pontuacao} pontos")

