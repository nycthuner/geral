while True:
    escolha=input("Escolha uma função:\n1-Index\n2-Count\n3-Copy\n4-Remove\n5-Pop\n6-Extend\n7-Insert\n8-Sort: ")
    if not "1" in escolha and not "2" in escolha and not "3" in escolha and not "4" in escolha and not "5" in escolha and not "6" in escolha and not "7" in escolha and not "8" in escolha:
        continue
    break
if escolha == "1":
    jubileu=["Jubileia" , "Kilua" , "nyc" ,"pato" , "phe" , "ana"]
    kilua=input("Digite um nome de endereço que voce que saber:")
    for i, e in enumerate(jubileu):
        if kilua == jubileu[i]:
            print(e)
            print(i)
            #e valor de cada um
            #endereço de cada um index
elif escolha == "2":
    jubileu=["Jubileia" , "Kilua" , "nyc" ,"pato" , "phe" , "ana"]
    kilua =  input("Qual o nome quer ver?")
    gon=0
    for i,e in enumerate(jubileu):
        if jubileu[i]==kilua:
            gon+=1
    print(gon)
elif escolha == "3":
    #i endereço do elemento no array
    #e valor do elemento no array
    jubileu=["Jubileia" , "Kilua" , "nyc" ,"pato" , "phe" , "ana"]
    kilua =  input("Quer copiar? ")
    for i in jubileu:
        if kilua == "sim" or kilua =="Sim":
            kilua = jubileu
            print(kilua)
            break
        else:
            print("Favor escrever sim")
            break
elif escolha == "4":
    jubileu=["Jubileia" , "Kilua" , "nyc" ,"pato" , "phe" , "ana"]
    kilua =  input("Quer deletar qual valor?")
    for i,e in enumerate(jubileu):
        if e == kilua:
            del jubileu[i]
            print(jubileu)
elif escolha == "5":
    jubileu=["Jubileia" , "Kilua" , "nyc" ,"pato" , "phe" , "ana"]
    kilua =  input("Funcao pop, escolhe ai: ")
    for i,e in enumerate(jubileu):
        if kilua == "":
            jubileu.reverse()
            del jubileu[i]
            jubileu.reverse()
            print(jubileu)
            break
        elif e == kilua:
            del jubileu[i]
            gon=i
            print(jubileu)
            print(gon)
elif escolha =="6":
    jubileu=["Jubileia" , "Kilua" , "nyc" ,"pato" , "phe" , "ana"]
    extend = 0
    array = []
    while True:
        kilua=input("Digita um nome: ")
        gon = input("Deseja continuar com mais nomes: sim/nao =>")
        array.append(kilua)
        if gon =="sim":
            continue
        elif  gon =="nao":
            break
        elif gon !="sim" and gon !="nao" :
            print("Escreve direito")
            continue
    for e in array:
        jubileu.append(array)
    print(jubileu)
elif escolha=="7":
    #i endereço do elemento no array
    #e valor do elemento no array
    jubileu=["Jubileia" , "Kilua" , "nyc" ,"pato" , "phe" , "ana"]
    gojo =  input("O que deseja inserir: ")
    satoru = int(input("Qual a posicao?"))
    for i,e in enumerate(jubileu):
        kaisen=jubileu[satoru]
        jubileu[satoru] = gojo
        break
    jubileu.append(kaisen)
    print(jubileu)
else:
    jubileu=["Jubileia" , "Kilua" , "nyc" ,"pato" , "phe" , "ana"]
    caracteresEspeciais = ['!', '@', '#', '$', '%', '&', '*', '+', '-', '=', '_', '`', '~', '^', '|', '\\', ']', '}', '{', '[', ':', ';', '"', '\'', '<', '>', '?', '.', ',']
    especial=[]
    num=[]
    maiusculo=[]
    minusculo=[]
    for e in jubileu:
        if e[0].islower():
            minusculo.append(e)
        elif e[0].isupper():
            maiusculo.append(e)
        elif any(char in e for char in caracteresEspeciais):
            especial.append(e)
        elif e.isdigit():
            num.append(e)
    print(especial)
    print(num)
    print(maiusculo)
    print(minusculo)