import os
login={
    "nycolas":"senha123456",
}
while True:
    usuario= input("Voce deseja fazer login ou cadastrar?")
    if not "login" in usuario and not "cadastrar" in usuario:
        continue
    break
if usuario == "login":
    usename = input("Digite seu nome de usuario: ")
    senha=input("Sua senha: ")
    
    for k,v in login.items():
        if usename == k:
            passw=login.keys()
            if senha == v:
                print("login feito")
                conf=True
        else:
            print("Deu errado tente novamente depois")
else:
    nome=input("Digite seu nome: ")
    pasw=input("Digite sua senha: ")
    login[nome] = pasw
    conf = True
os.system("clear")
while conf:
        while True:
            escolha = input("O que deseja fazer com o banco de dados?\n1-apagar\n2-adicionar\n3-editar\n4-visualizar\n5-pesquisar\n6-sair: ")
            if not "1" in escolha and not "2" in escolha and not "3" in escolha and not "4" in escolha and not "5" in escolha and not "6" in escolha:
                continue
            break
        while True:
            if escolha == "7":
                escolha = input("O que deseja fazer com o banco de dados?\n1-apagar\n2-adicionar\n3-editar\n4-visualizar\n5-pesquisar\n6-sair: ")
            else:   
                if  escolha=="1":
                    os.system("clear")
                    print(login)
                    apagar=input("Escolha qual item deseja apagar: ")
                    del login[apagar]
                    print(login)
                    escolha="7"
                elif escolha=="2":
                    os.system("clear")
                    addnome=input("Digite seu nome: ")
                    addsenha=input("Digite sua senha: ")
                    login[addnome]=addsenha
                    print(login)
                    escolha="7"
                elif escolha =="3":
                    os.system("clear")
                    print(login)
                    editar=input("Escolha qual item deseja editar: ")
                    for k,v in login.items():
                        if editar == k:
                            edicao=input("Edite agora o que deseja: ")
                            login[editar]=edicao
                            break
                        else:
                            print("Nao ha este item")
                    escolha="7"
                elif escolha == "4":
                    print(login)
                    escolha="7"
                elif escolha=="5":
                    print(login)
                    pes=input("Qual item deseja pesquisar? ")
                    for k,v in login.items():
                        if pes == k:
                            print(v)
                            break
                        else:
                            print("Nao tem este item")
                    escolha="7"
                elif escolha=="6":
                    exit()
                else:
                    continue