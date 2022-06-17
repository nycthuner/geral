dinheiro = float(input("Quanto voce quer transformar em dolares: "))
dolar = dinheiro/4.98
pergunta = input("Voce quer o valor inteiro ou com centavos: Sim ou Nao: ")

if "Sim" in pergunta or "sim" in pergunta:
    print(dolar)
else: 
    print(f"{dolar:.0f}")