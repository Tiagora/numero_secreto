pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print(pessoa)

pessoa = dict(nome="João", idade=30, cidade="São Paulo")
print(pessoa)

pessoa["telefone"] = "123456789"
print(pessoa)

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "987654321"},
    "maria@gmail.com": {"nome": "Maria", "telefone": "987654322"},
    "joao@gmail.com": {"nome": "João", "telefone": "987654323"},
    "ana@gmail.com": {"nome": "Ana", "telefone": "987654324", "extra":{"a":1}},
}

telefone = contatos["ana@gmail.com"]["telefone"]
print(telefone)

extra = contatos["ana@gmail.com"]["extra"]
print(extra)

for chave in contatos:
    print("1:" + chave, contatos[chave])

for chave, valor in contatos.items():
    print("2:" + chave, valor)

copia = contatos.copy()
copia["ana@gmail.com"] = {"nome":"Gui"}
print(copia)

print(dict.fromkeys(["nome", "idade", "telefone"]))

print(contatos.get("chave",{}))

print(contatos.keys())