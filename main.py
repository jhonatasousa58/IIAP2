lista_perguntas = ['Nome: ',
					'Idade(Somente numeros. Se recem-nascido/Neonato colocar: 0.1): ',
					'Febre acima de 38 Graus(sim ou nao): ',
					'Quantos dias de febre(1, 2, 3, ...): ',
					'Manchas na pele(sim ou nao): ',
					'Surgiu a partir de qual dia(1, 2, 3, ...): ',
					'Frequencia da dor nos musculos(0 - Nenhuma, 1 - Leve, 2 - Moderada ou 3 - Intensa): ',
					'Frequencia da dor na Articulacao(0 - Nenhum, 1 - Leve, 2 - Moderada ou 3 - Intensa): ',
					'Intensidade da dor articular(0 - Nenhuma, 1 - Leve, 2 - Leve/Moderada, 3 - Moderada/Intensa): ',
					'Edema da articulacao(1 - Nao/Raro, 2 - Frequente e leve Intensidade, 3 - Frequente e de moderada a Intensa): ',
					'Conjuntivite(sim ou nao): ',
					'Dor de cabeca - Frequencia e Intensidade(0 - Nenhuma, 1 - Leve, 2 - Moderada ou 3 - Intensa): ',
					'Coceira(0 - Nenhuma, 1 - Leve, 2 - Moderada ou 3 - Intensa): ',
					'Frequencia hipertrofia ganglionar(0 - Nenhuma, 1 - Leve, 2 - Moderada ou 3 - Intensa): ',
					'Frequencia discrasia hemorragica(0 - Nenhuma, 1 - Ausente, 2 - Leve ou 3 - Moderada): ',
					'Acometimento Neurologico(sim ou nao): ']

probabilidades_Sintomas = [
	[1.0, 1.0, 1.0, 1.0],
	[1.0, 1.0, 1.0, 1.0],
	[1.0, 1.0, 1.0, 1.0],
	[1.0, 1.0, 1.0, 1.0],
	[1.0, 1.0, 1.0, 1.0],
	[1.0, 1.0, 1.0, 1.0],
	[1.0, 1.0, 1.0, 1.0],
	[1.0, 1.0, 1.0, 1.0],
	[1.0, 1.0, 1.0, 1.0],
	[1.0, 1.0, 1.0, 1.0],
	[1.0, 1.0, 1.0, 1.0],
	[1.0, 1.0, 1.0, 1.0],
	[1.0, 1.0, 1.0, 1.0],
]

probabilidades_Hipoteses = [0, 0, 0, 0]

Hdengue = 0
Hzika = 1
Hchikungunya = 2
Hnada = 3
i = 0
while(i < len(lista_perguntas)):
	res = input(lista_perguntas[i])
	if(lista_perguntas[i] == lista_perguntas[0]):
		nome = res

	elif(lista_perguntas[i] == lista_perguntas[1]):
		idade = int(res)

	elif(lista_perguntas[i] == lista_perguntas[2]):
		if(res == 'sim'):
			probabilidades_Sintomas[i-2][Hdengue] = 1.0
			probabilidades_Sintomas[i-2][Hzika] = 0.2
			probabilidades_Sintomas[i-2][Hchikungunya] = 1.0
			probabilidades_Sintomas[i-2][Hnada] = 0.1
		elif(res == 'nao'):
			probabilidades_Sintomas[i-2][Hdengue] = 0.1
			probabilidades_Sintomas[i-2][Hzika] = 1.0
			probabilidades_Sintomas[i-2][Hchikungunya] = 0.1
			probabilidades_Sintomas[i-2][Hnada] = 1.0
			i += 1

	elif(lista_perguntas[i] == lista_perguntas[3]):
		if(2 <= int(res) <= 3):
			probabilidades_Sintomas[i-3][Hdengue] = 0.3
			probabilidades_Sintomas[i-3][Hzika] = 0.2
			probabilidades_Sintomas[i-3][Hchikungunya] = 1.0
			probabilidades_Sintomas[i-3][Hnada] = 0.1
		if(int(res) >= 4):
			probabilidades_Sintomas[i-3][Hdengue] = 1.0
			probabilidades_Sintomas[i-3][Hzika] = 0.2
			probabilidades_Sintomas[i-3][Hchikungunya] = 0.3
			probabilidades_Sintomas[i-3][Hnada] = 0.1

	elif(lista_perguntas[i] == lista_perguntas[4]):
		if(res == 'nao'):
			i += 1

	elif(lista_perguntas[i] == lista_perguntas[5]):
		if(1 <= int(res) <= 2):
			probabilidades_Sintomas[i-4][Hdengue] = 0.2
			probabilidades_Sintomas[i-4][Hzika] = 1.0
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.3
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(3 <= int(res) <= 5):
			probabilidades_Sintomas[i-4][Hdengue] = 0.3
			probabilidades_Sintomas[i-4][Hzika] = 0.2
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.5
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(int(res) > 5):
			probabilidades_Sintomas[i-4][Hdengue] = 0.5
			probabilidades_Sintomas[i-4][Hzika] = 0.2
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.3
			probabilidades_Sintomas[i-4][Hnada] = 0.1

	elif(lista_perguntas[i] == lista_perguntas[6]):
		if(int(res) == 0):
			probabilidades_Sintomas[i-4][Hdengue] = 0.1
			probabilidades_Sintomas[i-4][Hzika] = 0.1
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.2
			probabilidades_Sintomas[i-4][Hnada] = 1.0
		if(int(res) == 1):
			probabilidades_Sintomas[i-4][Hdengue] = 0.33
			probabilidades_Sintomas[i-4][Hzika] = 0.66
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.99
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(int(res) == 2):
			probabilidades_Sintomas[i-4][Hdengue] = 0.66
			probabilidades_Sintomas[i-4][Hzika] = 0.99
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.33
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(int(res) == 3):
			probabilidades_Sintomas[i-4][Hdengue] = 0.99
			probabilidades_Sintomas[i-4][Hzika] = 0.66
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.33
			probabilidades_Sintomas[i-4][Hnada] = 0.1

	elif(lista_perguntas[i] == lista_perguntas[7]):
		if(int(res) == 0):
			probabilidades_Sintomas[i-4][Hdengue] = 0.1
			probabilidades_Sintomas[i-4][Hzika] = 0.1
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.2
			probabilidades_Sintomas[i-4][Hnada] = 1.0
		if(int(res) == 1):
			probabilidades_Sintomas[i-4][Hdengue] = 0.33
			probabilidades_Sintomas[i-4][Hzika] = 0.66
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.99
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(int(res) == 2):
			probabilidades_Sintomas[i-4][Hdengue] = 0.66
			probabilidades_Sintomas[i-4][Hzika] = 0.99
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.33
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(int(res) == 3):
			probabilidades_Sintomas[i-4][Hdengue] = 0.99
			probabilidades_Sintomas[i-4][Hzika] = 0.66
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.33
			probabilidades_Sintomas[i-4][Hnada] = 0.1

	elif(lista_perguntas[i] == lista_perguntas[8]):
		if(int(res) == 0):
			probabilidades_Sintomas[i-4][Hdengue] = 0.1
			probabilidades_Sintomas[i-4][Hzika] = 0.1
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.2
			probabilidades_Sintomas[i-4][Hnada] = 1.0
		if(int(res) == 1):
			probabilidades_Sintomas[i-4][Hdengue] = 0.33
			probabilidades_Sintomas[i-4][Hzika] = 0.66
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.99
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(int(res) == 2):
			probabilidades_Sintomas[i-4][Hdengue] = 0.66
			probabilidades_Sintomas[i-4][Hzika] = 0.99
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.33
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(int(res) == 3):
			probabilidades_Sintomas[i-4][Hdengue] = 0.99
			probabilidades_Sintomas[i-4][Hzika] = 0.66
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.33
			probabilidades_Sintomas[i-4][Hnada] = 0.1

	elif(lista_perguntas[i] == lista_perguntas[9]):
		if(int(res) == 0):
			probabilidades_Sintomas[i-4][Hdengue] = 0.1
			probabilidades_Sintomas[i-4][Hzika] = 0.1
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.2
			probabilidades_Sintomas[i-4][Hnada] = 1.0
		if(int(res) == 1):
			probabilidades_Sintomas[i-4][Hdengue] = 0.33
			probabilidades_Sintomas[i-4][Hzika] = 0.66
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.99
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(int(res) == 2):
			probabilidades_Sintomas[i-4][Hdengue] = 0.66
			probabilidades_Sintomas[i-4][Hzika] = 0.99
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.33
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(int(res) == 3):
			probabilidades_Sintomas[i-4][Hdengue] = 0.99
			probabilidades_Sintomas[i-4][Hzika] = 0.66
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.33
			probabilidades_Sintomas[i-4][Hnada] = 0.1

	elif(lista_perguntas[i] == lista_perguntas[10]):
		if(res == 'sim'):
			probabilidades_Sintomas[i-4][Hdengue] = 0.2
			probabilidades_Sintomas[i-4][Hzika] = 0.9
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.3
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		else:
			probabilidades_Sintomas[i-4][Hdengue] = 0.9
			probabilidades_Sintomas[i-4][Hzika] = 0.2
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.3
			probabilidades_Sintomas[i-4][Hnada] = 0.8

	elif(lista_perguntas[i] == lista_perguntas[11]):
		if(int(res) == 0):
			probabilidades_Sintomas[i-4][Hdengue] = 0.1
			probabilidades_Sintomas[i-4][Hzika] = 0.1
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.2
			probabilidades_Sintomas[i-4][Hnada] = 1.0
		if(int(res) == 1):
			probabilidades_Sintomas[i-4][Hdengue] = 0.33
			probabilidades_Sintomas[i-4][Hzika] = 0.66
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.99
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(int(res) == 2):
			probabilidades_Sintomas[i-4][Hdengue] = 0.66
			probabilidades_Sintomas[i-4][Hzika] = 0.99
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.33
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(int(res) == 3):
			probabilidades_Sintomas[i-4][Hdengue] = 0.99
			probabilidades_Sintomas[i-4][Hzika] = 0.66
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.33
			probabilidades_Sintomas[i-4][Hnada] = 0.1

	elif(lista_perguntas[i] == lista_perguntas[12]):
		if(int(res) == 0):
			probabilidades_Sintomas[i-4][Hdengue] = 0.1
			probabilidades_Sintomas[i-4][Hzika] = 0.1
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.2
			probabilidades_Sintomas[i-4][Hnada] = 1.0
		if(int(res) == 1):
			probabilidades_Sintomas[i-4][Hdengue] = 0.33
			probabilidades_Sintomas[i-4][Hzika] = 0.66
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.99
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(int(res) == 2):
			probabilidades_Sintomas[i-4][Hdengue] = 0.66
			probabilidades_Sintomas[i-4][Hzika] = 0.99
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.33
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(int(res) == 3):
			probabilidades_Sintomas[i-4][Hdengue] = 0.99
			probabilidades_Sintomas[i-4][Hzika] = 0.66
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.33
			probabilidades_Sintomas[i-4][Hnada] = 0.1

	elif(lista_perguntas[i] == lista_perguntas[13]):
		if(int(res) == 0):
			probabilidades_Sintomas[i-4][Hdengue] = 0.1
			probabilidades_Sintomas[i-4][Hzika] = 0.1
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.2
			probabilidades_Sintomas[i-4][Hnada] = 1.0
		if(int(res) == 1):
			probabilidades_Sintomas[i-4][Hdengue] = 0.33
			probabilidades_Sintomas[i-4][Hzika] = 0.66
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.99
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(int(res) == 2):
			probabilidades_Sintomas[i-4][Hdengue] = 0.66
			probabilidades_Sintomas[i-4][Hzika] = 0.99
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.33
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(int(res) == 3):
			probabilidades_Sintomas[i-4][Hdengue] = 0.99
			probabilidades_Sintomas[i-4][Hzika] = 0.66
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.33
			probabilidades_Sintomas[i-4][Hnada] = 0.1

	elif(lista_perguntas[i] == lista_perguntas[14]):
		if(int(res) == 0):
			probabilidades_Sintomas[i-4][Hdengue] = 0.1
			probabilidades_Sintomas[i-4][Hzika] = 0.1
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.2
			probabilidades_Sintomas[i-4][Hnada] = 1.0
		if(int(res) == 1):
			probabilidades_Sintomas[i-4][Hdengue] = 0.33
			probabilidades_Sintomas[i-4][Hzika] = 0.66
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.99
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(int(res) == 2):
			probabilidades_Sintomas[i-4][Hdengue] = 0.66
			probabilidades_Sintomas[i-4][Hzika] = 0.99
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.33
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(int(res) == 3):
			probabilidades_Sintomas[i-4][Hdengue] = 0.99
			probabilidades_Sintomas[i-4][Hzika] = 0.66
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.33
			probabilidades_Sintomas[i-4][Hnada] = 0.1

	elif(lista_perguntas[i] == lista_perguntas[15]):
		if(res == 'sim'):
			probabilidades_Sintomas[i-4][Hdengue] = 0.2
			probabilidades_Sintomas[i-4][Hzika] = 0.6
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.2
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		if(res == 'sim' and idade == 0.1):
			probabilidades_Sintomas[i-4][Hdengue] = 0.2
			probabilidades_Sintomas[i-4][Hzika] = 0.6
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.7
			probabilidades_Sintomas[i-4][Hnada] = 0.1
		else:
			probabilidades_Sintomas[i-4][Hdengue] = 0.7
			probabilidades_Sintomas[i-4][Hzika] = 0.3
			probabilidades_Sintomas[i-4][Hchikungunya] = 0.7
			probabilidades_Sintomas[i-4][Hnada] = 0.6

	i += 1



probabilidadep = 1
divisor = 0
for coluna in range(4):
	for linha in range(13):
		probabilidadep *= probabilidades_Sintomas[linha][coluna]
	probabilidades_Hipoteses[coluna] = probabilidadep
	divisor += probabilidadep
	probabilidadep = 1

for k in range(4):
	probabilidades_Hipoteses[k] = probabilidades_Hipoteses[k]/divisor;

dengue = probabilidades_Hipoteses[0]
zika = probabilidades_Hipoteses[1]
chik = probabilidades_Hipoteses[2]
nada = probabilidades_Hipoteses[3]

resultado = max(dengue, zika, chik, nada)

print("Nome: ",nome, "idade: ",idade, "ano(s). Diagnostico: Dengue com ", dengue*100, " de porcentagem")	
print("Nome: ",nome, "idade: ",idade, "ano(s). Diagnostico: Zika com ", zika*100, " de porcentagem")	
print("Nome: ",nome, "idade: ",idade, "ano(s). Diagnostico: Chikungunya com ", chik*100, " de porcentagem")	
print("Nome: ",nome, "idade: ",idade, "ano(s). Diagnostico: Nada com ", nada*100, " de porcentagem")	
