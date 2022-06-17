usuario = input("Usuario: ")
senha = input("Sua senha: ")

if len(usuario) == 8 and not "#" in usuario and not "!" in usuario:
    if len(senha) == 8 and  "#" in senha or  "!" in senha:
        print("Conta criada")
    else:
        senha = input("Sua senha novamente: ")
        if len(senha)== 8 and "#" in senha or "!" in senha:
            print("Conta criada com sucesso")
        else:
            print("Nao mexe mais") 
else:
    usuario = input("Digite usuario corretamente: ")
    if len(usuario) == 8 and not "#" in usuario and not "!" in usuario:
        if len(senha) == 8 and "#" in senha or "!" in senha:
            print("Conta criada")
        else:
            senha = input("Sua senha novamente: ")
            if len(senha)== 8 and "#" in senha or "!" in senha:
                print("Conta criada com sucesso")
            else:
                print("Nao mexe mais") 
    else:
        print("Nao vai criar mais")
