casos = int(input())
for _ in range(casos):
    caso = input()
    primeira_passada = ""
    for letra in caso:
        #primeira passada
        if letra.isalpha(): #verifica se é uma letra
            letra = chr(ord(letra)+3)
            primeira_passada+=letra
        else:
            primeira_passada+=letra
    segunda_passada = primeira_passada[::-1] #inverte, como é pedido na segunda passada
    #terceira passada
    terceira_passada = ""
    metade_palavra = len(segunda_passada)//2
    for i in range(len(segunda_passada)):
        if i >= metade_palavra:
            terceira_passada+= chr(ord(segunda_passada[i])-1)
        else: terceira_passada+= segunda_passada[i]
    print(terceira_passada)
        
#chr(): converte um código Unicode ou ASCII em um caractere
#ord(): converte um caractere em ASCII