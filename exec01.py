n = int(input("Digite um numero: "))
num = 1
while num<11:
    if n%num==0:
        print("Multiplo de: " ,num)
    else:
        print("Nao e multiplo de: " ,num)
    num+=1