from datetime import date, datetime, time, timedelta

data = date(2024, 6, 1)
print(data)
print(data.today())


data_hora = datetime(2024, 6, 1)
print(data_hora)

hora = time(14, 30, 0)
print(hora)

tipo_carro = "P"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro =="P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto ás {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto ás {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto ás {data_estimada}")

print(date.today()- timedelta(days=699999))