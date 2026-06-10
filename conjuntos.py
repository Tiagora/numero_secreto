print(set ([1, 5,2, 3, 4, 1, 2, 5]))

linguagens = {"Python", "Java", "C", "C++", "Python", "Java"}
print(linguagens)

numeros = {1, 2, 3, 4, 5}
numeros = list(numeros)
print(numeros[0])

carros = {"Fusca", "Brasilia", "Chevette", "Fusca"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4,5,6, 7, 8,9,10}

print(conjunto_a.union(conjunto_b))
print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
print(conjunto_a.symmetric_difference(conjunto_b))
print(conjunto_a.issubset(conjunto_b))
print(conjunto_a.issuperset(conjunto_b)) 
print(conjunto_b.issubset(conjunto_a))
print(conjunto_b.issuperset(conjunto_a)) 
print(conjunto_a.isdisjoint(conjunto_b))  
print(conjunto_a.add(7))