from datetime import datetime   

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20:30"
mascara_ptbr = "%d/%m/%Y %a %H:%M:%S"
mascara_en = "%Y-%m-%d %H:%M:%S"

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida.strftime(mascara_en))
print(type(data_convertida))