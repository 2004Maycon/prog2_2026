def main():
    quantms = 0
    quantfs = 0
    somaridade45mais=0
    f35menoscomexp=0
    idade_mas45 = 0
    totalmais45 = 0
    menor_idade = 999
    incricao_menor_idade = 0
    candidato = int(input("qual seu numero: "))
    while candidato != 0:
        idade = int(input("digite sua idade: "))
        sexo = input("digite sua sexualidade(m/f): ") 
        experiencia = input("voce tem experiencia (sim,nao): ").lower() == "sim"
        #atualiza os quantificadores
        if sexo == "f":
            if experiencia:
                if idade < 35:
                    f35menoscomexp+=1
                if idade < menor_idade:
                    menor_idade=idade
                    incricao_menor_idade = candidato
            quantfs+=1
        elif sexo == "m":
            if idade > 45:
                idade_mas45 += idade
                totalmais45+= 1
            quantms += 1
        print("---"*25)
        candidato = int(input("qual seu numero: "))
#exibir as estatisticas (quantificadores)
    print("---"*25)
    print(f"quantos mulheres: {quantfs}")
    print(f"quantos homens: {quantms}")
    print(f"media de idade de homens mais 45: {idade_mas45/totalmais45 :.2f}")
    print(f"total de mulher menor de 35: {f35menoscomexp}")
    print(f" menor idade: {menor_idade}")
    print(f"inscriçao da mulher menor idade: {incricao_menor_idade}")
main()
    