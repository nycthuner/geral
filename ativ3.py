brancos = int(input("Numero de votos em branco: "))
nulos = int(input("Numero de votos nulos: "))
validos = int(input("Numero de votos validos: "))
percentbranco = brancos/100
percentnulo = nulos/100
percentvalidos = validos/100
votos = brancos + nulos + validos
print(votos)
print(percentbranco)
print(percentnulo)
print(percentvalidos)