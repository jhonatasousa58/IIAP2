def fuzzyfication(probabilidades_sintomas):
    Hdengue = 0
    Hzika = 1
    Hchikungunya = 2
    Hnada = 3

    nome = input("Nome: ")
    idade = int(input("Idade(Somente numeros. Se recem-nascido/Neonato colocar: 0.1): "))

    for i in range(12):
        # Sintoma Febre
        if (i == 0):
            res = input("Voce tem Febre ? (sim ou nao): ").lower()
            # Se nao tiver febre, atribui as probabilidades de ter zika e nada
            if (res == 'nao'):
                probabilidades_sintomas[i][Hzika] = 1.0
                probabilidades_sintomas[i][Hnada] = 1.0

            # Se tiver febre, pergunta se é acima de 38 graus e a quantidade de dias
            elif (res == 'sim'):
                res = input("Acima de 38 Graus ? (sim ou nao): ").lower()
                res1 = int(input("Quantos dias de febre(1, 2, 3, ...): "))
                if (res == 'sim'):
                    if (4 <= res1 <= 7):
                        probabilidades_sintomas[i][Hdengue] = 1.0
                    elif (2 <= res1 <= 3):
                        probabilidades_sintomas[i][Hchikungunya] = 1.0
                    else:
                        probabilidades_sintomas[i][Hnada] = 1.0
                elif (res == 'nao'):
                    if (1 <= res1 <= 2):
                        probabilidades_sintomas[i][Hzika] = 1.0

        # Sintoma Manchas
        elif (i == 1):
            # Distribui as probabilidades de acordo com a quatidade de dias que as manchas apareceram
            res = int(input("Manchas a partir de quantos dias(0 - se nao houver manchas na pele): "))
            if (res == 0):
                probabilidades_sintomas[i][Hnada] = 1.0
            elif (res > 0):
                if (res >= 4):
                    probabilidades_sintomas[i][Hdengue] = 0.4
                if (1 <= res <= 2):
                    probabilidades_sintomas[i][Hzika] = 0.95
                if (2 <= res <= 5):
                    probabilidades_sintomas[i][Hchikungunya] = 0.5

        # Sintoma Dor no musculos
        elif (i == 2):
            # Distribui as probabilidades de acordo com a frequencia da dor no musculos
            res = int(input("Frequencia da dor nos musculos(0 - Nenhuma, 1 - +, 2 - ++ ou 3 - +++): "))
            if (res == 0):
                probabilidades_sintomas[i][Hnada] = 1.0
            elif (res == 1):
                probabilidades_sintomas[i][Hchikungunya] = 1.0
            elif (res == 2):
                probabilidades_sintomas[i][Hzika] = 1.0
            elif (res == 3):
                probabilidades_sintomas[i][Hdengue] = 1.0

        # Sintoma Dor na articulçao
        elif (i == 3):
            # Distribui as probabilidades de acordo com a frequencia da dor na articulacao
            res = int(input("Frequencia da dor na Articulacao(0 - Nenhum, 1 - +, 2 - ++ ou 3 - +++): "))
            if (res == 0):
                probabilidades_sintomas[i][Hnada] = 1.0
            elif (res == 1):
                probabilidades_sintomas[i][Hdengue] = 1.0
            elif (res == 2):
                probabilidades_sintomas[i][Hzika] = 1.0
            elif (res == 3):
                probabilidades_sintomas[i][Hchikungunya] = 1.0

        # Sintoma Intensidade Dor na articulçao
        elif (i == 4):
            # Distribui as probabilidades de acordo com a intensidade da dor na articulacao
            res = int(
                input("Intensidade da dor articular(0 - Nenhuma, 1 - Leve, 2 - Leve/Moderada, 3 - Moderada/Intensa): "))
            if (res == 0):
                probabilidades_sintomas[i][Hnada] = 1.0
            elif (res == 1):
                probabilidades_sintomas[i][Hdengue] = 1.0
            elif (res == 2):
                probabilidades_sintomas[i][Hzika] = 1.0
            elif (res == 3):
                probabilidades_sintomas[i][Hchikungunya] = 1.0

        # Sintoma Edema da articulçao
        elif (i == 5):
            # Distribui as probabilidades de acordo com edema da articulacao
            res = int(input(
                "Edema da articulacao(1 - Nao, 2 - Frequente e leve Intensidade, 3 - Frequente e de moderada a Intensa): "))

            if (res == 1):
                probabilidades_sintomas[i][Hnada] = 1.0
            elif (res == 2):
                probabilidades_sintomas[i][Hdengue] = 0.1
                probabilidades_sintomas[i][Hzika] = 1.0
            elif (res == 3):
                probabilidades_sintomas[i][Hdengue] = 0.1
                probabilidades_sintomas[i][Hchikungunya] = 1.0

        # Sintoma Conjuntivite
        elif (i == 6):
            # Distribui as probabilidades de acordo com as chances de ter determinada doenca
            res = input("Conjuntivite(sim ou nao): ").lower()
            if (res == 'sim'):
                probabilidades_sintomas[i][Hdengue] = 0.1
                probabilidades_sintomas[i][Hzika] = 0.7
                probabilidades_sintomas[i][Hchikungunya] = 0.3
            elif (res == 'nao'):
                probabilidades_sintomas[i][Hnada] = 1.0

        # Sintoma Frequencia e Intensidade Dor de Cabeca
        elif (i == 7):
            # Distribui as probabilidades de acordo com a intensidade da dor na articulacao
            res = int(input("Dor de cabeca - Frequencia e Intensidade(0 - Nenhuma, 1 - +, 2 - ++ ou 3 - +++): "))
            if (res == 0 or res == 1):
                probabilidades_sintomas[i][Hnada] = 1.0
            elif (res == 2):
                probabilidades_sintomas[i][Hzika] = 1.0
                probabilidades_sintomas[i][Hchikungunya] = 1.0
            elif (res == 3):
                probabilidades_sintomas[i][Hdengue] = 1.0

        # Sintoma Coceira
        elif (i == 8):
            # Distribui as probabilidades de acordo com a intensidade da coceira
            res = int(input("Coceira(0 - Nenhuma, 1 - Leve, 2 - Moderada ou 3 - Intensa): "))
            if (res == 0):
                probabilidades_sintomas[i][Hnada] = 1.0
            elif (res == 1):
                probabilidades_sintomas[i][Hdengue] = 1.0
                probabilidades_sintomas[i][Hchikungunya] = 1.0
            elif (res == 2 or res == 3):
                probabilidades_sintomas[i][Hchikungunya] = 1.0

        # Sintoma Hipertrofia Ganglionar
        elif (i == 9):
            # Distribui as probabilidades de acordo com a frequencia da Hipertrofia Ganglionar
            res = int(input("Frequencia hipertrofia ganglionar(0 - Nenhuma, 1 - Leve, 2 - Moderada ou 3 - Intensa): "))
            if (res == 0):
                probabilidades_sintomas[i][Hnada] = 1.0
            elif (res == 1):
                probabilidades_sintomas[i][Hdengue] = 1.0
            elif (res == 2):
                probabilidades_sintomas[i][Hchikungunya] = 1.0
            elif (res == 3):
                probabilidades_sintomas[i][Hzika] = 1.0

        # Sintoma Discrasia Hemorragica
        elif (i == 10):
            # Distribui as probabilidades de acordo com a frequencia da discrasia hemorragica
            res = int(input("Frequencia discrasia hemorragica(1 - Ausente, 2 - Leve ou 3 - Moderada): "))
            if (res == 0 or res == 1):
                probabilidades_sintomas[i][Hnada] = 1.0
                probabilidades_sintomas[i][Hzika] = 1.0
            elif (res == 2):
                probabilidades_sintomas[i][Hchikungunya] = 1.0
            elif (res == 3):
                probabilidades_sintomas[i][Hdengue] = 1.0

        # Sintoma Acometimento Neurologico
        elif (i == 11):
            # Distribui as probabilidades de acordo com o Acometimento Neurologico
            res = input("Acometimento Neurologico(sim ou nao): ").lower()
            if (res == 'sim'):
                probabilidades_sintomas[i][Hdengue] = 0.1
                probabilidades_sintomas[i][Hzika] = 0.3
                probabilidades_sintomas[i][Hchikungunya] = 0.1
            elif (res == 'sim' and idade == 0.1):
                probabilidades_sintomas[i][Hchikungunya] = 0.5
            elif (res == 'nao'):
                probabilidades_sintomas[i][Hnada] = 1.0

        i += 1

    return nome, idade, probabilidades_sintomas


def bayes(probabilidades_sintomas):
    probabilidadep = 1
    divisor = 0
    probabilidades_hipoteses = [0, 0, 0, 0]

    for coluna in range(4):
        for linha in range(13):
            probabilidadep *= probabilidades_sintomas[linha][coluna]
        probabilidades_hipoteses[coluna] = probabilidadep
        divisor += probabilidadep
        probabilidadep = 1

    for k in range(4):
        probabilidades_hipoteses[k] = probabilidades_hipoteses[k] / divisor

    return probabilidades_hipoteses


def run(probabilidades_sintomas):
    nome, idade, probabilidades_sintomas = fuzzyfication(probabilidades_sintomas)

    probabilidades_hipoteses = bayes(probabilidades_sintomas)

    hipoteses = [["Dengue", probabilidades_hipoteses[0]],
                 ["Zika", probabilidades_hipoteses[1]],
                 ["Chikungunya", probabilidades_hipoteses[2]],
                 ["Nenhuma", probabilidades_hipoteses[3]]]

    resultado = max(hipoteses[0][1], hipoteses[1][1], hipoteses[2][1], hipoteses[3][1])

    i=0
    while hipoteses[i][1] != resultado:
        i += 1

    print("|---------------------------- Paciente -----------------------------|")
    print("Nome: ", nome)
    print("Idade: ", idade)
    print("|---------------------------- Resultado ----------------------------|")
    print("   Diagnostico: {} com {:.2f} de porcentagem".format(hipoteses[i][0], hipoteses[i][1] * 100))
    print()

    print("|---------------------- Outras possibilidades ----------------------|")
    print("Nome: ", nome, "idade: ", idade, "ano(s). Diagnostico: {} com {:.6f} de porcentagem".format(hipoteses[0][0], hipoteses[0][1] * 100))
    print("Nome: ", nome, "idade: ", idade, "ano(s). Diagnostico: {} com {:.6f} de porcentagem".format(hipoteses[1][0], hipoteses[1][1] * 100))
    print("Nome: ", nome, "idade: ", idade, "ano(s). Diagnostico: {} com {:.6f} de porcentagem".format(hipoteses[2][0], hipoteses[2][1] * 100))
    print("Nome: ", nome, "idade: ", idade, "ano(s). Diagnostico: {} com {:.6f} de porcentagem".format(hipoteses[3][0], hipoteses[3][1] * 100))
