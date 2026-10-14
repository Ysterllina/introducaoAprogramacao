#def nome_funcao(a: int, b:int) -> int:
    #processamento
    #return

#ccada funcao deve ter apenas uma tarefa
#def significa definicion (palavra reservada para definir funcao)
def soma(x:int, y:int) -> int:
    resultado: int = x + y
    return resultado
# as variaveis dentro da funcao n podem ser acessadas fora

resultado: int = soma(10, 20)
print(resultado)
