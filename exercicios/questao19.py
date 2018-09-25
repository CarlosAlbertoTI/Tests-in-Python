def converterTempo(horas,minutos):
	if horas <= 12 :
		meio_dia = 'AM'
		MostrarHora(horas,minutos,meio_dia)
	elif 12 < horas <= 23:
		meio_dia = 'PM'
		hora = horas - 12
		MostrarHora(hora,minutos,meio_dia)
	elif horas == 24:
		meio_dia = 'AM'
		horas = '00'
		MostrarHora(horas,minutos,meio_dia)

def MostrarHora(hora,minuto,meio_dia):
	if meio_dia == 'AM':
		print(hora,':',minuto,' ',meio_dia)
	else:
		print(hora,':',minuto,' ',meio_dia)


hora = int( input('Digite a hora em formato de 24Hrs: '))
minuto = int( input('Digite os minutos: '))

converterTempo(hora,minuto)

