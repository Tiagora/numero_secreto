frutas = ["maçã", "banana", "laranja", "uva"]
print(frutas)
print(frutas[0])  # Acessa o primeiro elemento
print(frutas[-1])  # Acessa o ultimo elemento

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

carros = ["Fusca", "Gol", "Corsa", "Palio", "Uno"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"Índice: {indice}, Carro: {carro}")

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)

quadrado = [numero ** 2 for numero in numeros]
print(quadrado)