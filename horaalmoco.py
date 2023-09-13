from datetime import datetime, timedelta

def calcular_horas_trabalhadas(entrada, saida, intervalo):
   try:
       if ":" not in entrada:
           entrada = entrada[:-2] + ":" + entrada[-2:]

 

       if ":" not in saida:
           saida = saida[:-2] + ":" + saida[-2:]

 

       entrada_dt = datetime.strptime(entrada, '%H:%M')
       saida_dt = datetime.strptime(saida, '%H:%M')

 

       diferenca = saida_dt - entrada_dt

 

       intervalo_dt = timedelta(hours=int(intervalo.split(":")[0]), minutes=int(intervalo.split(":")[1]))
       diferenca -= intervalo_dt

 

       horas, segundos = divmod(diferenca.seconds, 3600)
       minutos = segundos // 60

 

       return f"{horas} horas e {minutos} minutos"

 

   except ValueError:
       return "Formato de hora inválido. Use HH:mm ou HHmm."

 

hora_entrada = input("Informe a hora de entrada (HH:mm ou HHmm): ")
hora_saida = input("Informe a hora de saída (HH:mm ou HHmm): ")
duracao_intervalo = input("Informe a duração do intervalo de almoço (HH:mm ou HHmm): ")

 

resultado = calcular_horas_trabalhadas(hora_entrada, hora_saida, duracao_intervalo)
print(f"Horas trabalhadas: {resultado}")