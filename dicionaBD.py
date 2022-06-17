with open("BD_mochila.txt","w") as mochila:
    mochila.write("nycolas")
while True:
    login= input("Deseja fazer login?")
    if not "sim" in login and not "Sim" in login:
        continue
    break
with open("BD_mochila.txt","r") as BDmochila:
    username = input("Digite seu nome de login: ")
    seila=BDmochila.readline()
    print(seila)
    if username == seila:
        print("existe")
    else:
        print("nao existe")