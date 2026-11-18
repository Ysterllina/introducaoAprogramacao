# criar uma funcao que receba:
# nome completo
# senha
# confirmar senha

#login e validar senha
#login -> nome.sobrenome
#senha tem que ter:
#8 caracteres
#1 M
#1 m
#1 @
#1 digito
# senha e confirmação de senha tem ser ==

def autenficacao() -> bool:
    nome:str = input("Digite seu nome completo: ")
    # login: str = 
    # "Gabriela de Assis Oliveira"
    # login = Gabriela.Oliveira
    # concatena tudo
    # qnd tiver espaço, substitui o espaço por .
    # no ultimo espaço contatena tudo depois dele
    # assim vai ficar Gabriela.Oliveira
    # print(Gabriela.Oliveira)

    print("Instruções para criação de senha: \n\n" 
          
         "Sua senha deve ter ao menos:\n"
         "* Uma letra maiúscula.\n" 
         "* Uma letra minúscula.\n"
         "* Um caractere especial.\n"
         "* Um dígito.\n"
         "* 8 caracteres\n")
    
    senha:str = input("Digite sua senha: ")
    confirmacao:str = input("Digite sua senha para confirmação: ")

    if confirmacao == senha:

        MINUSCULAS: str = "abcdefghijklmnopqrstuvwxyz"
        MAIUSCULAS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        DIGITOS: str = "0123456789"
        CARACTERES_ESPECIAIS: str = "!@#$%¨&*()_+=-§"

    if len(senha) >= 8:

        tem_minuscula = False
        tem_maiuscula = False
        tem_digito = False
        tem_caractere_especial = False

        for caracter in senha:

            if caracter in MINUSCULAS:
                tem_minuscula = True

            if caracter in MAIUSCULAS:
                tem_maiuscula = True

            if caracter in DIGITOS:
                tem_digito = True

            if caracter in CARACTERES_ESPECIAIS:
                tem_caractere_especial = True

            if tem_minuscula and tem_maiuscula and tem_digito and tem_caractere_especial:
                return True


print(autenficacao())

