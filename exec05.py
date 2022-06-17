while True:
    usuario = input("Digite seu nome de usuario: ")
    if len(usuario)<11 or "!" in usuario and "#" in usuario and "" in usuario:
       continue
    break
while True:
    senha = input("Digite sua senha e somente com numeros: ")
    if len(senha)<8 and type(senha) !=int:
        continue
    else:
        print("Conta criada com sucesso")
    break