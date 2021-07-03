def mediaLista(lista):

    total = 0
    for num in range(len(lista)):
        total = total + lista[num]

    total = total/len(lista)
    return total

codigo = 1
lista = []

while(codigo != 0):
    numero = int(input("Insira o numero: "))
    lista.append(numero)
    codigo = int(input(("Se deseja parar digite 0, caso contrario 1: ")))

print(lista)
print(mediaLista(lista))