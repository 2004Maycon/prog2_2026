def main():
    maior_pontuacao = -1.0
    inscricao_vencedor = 0
    tempo_padrao = []
    for i in range(1, 4):
        tempo = float(input(f"Digite o tempo-padrão da etapa {i}: "))
        tempo_padrao.append(tempo)

    inscricao = int(input("Número de inscrição (9999 para encerrar): "))
    while inscricao != 9999:

        pontos_equipe = []
        for i in range(3):
            t_equipe = float(input(f"Digite o tempo da equipe na etapa {i+1}: "))
            D = tempo_padrao[i] - t_equipe
            if D < 3:
                p = 100.0
            elif D <= 5:
                p = 80.0
            else:
                p = 80.0 - (D - 5) / 5
            pontos_equipe.append(p)
        total_pontos = sum(pontos_equipe)
        print(f"Equipe: {inscricao}")
        print(f"Pontos Etapa 1: {pontos_equipe[0]:.2f} | Etapa 2: {pontos_equipe[1]:.2f} | Etapa 3: {pontos_equipe[2]:.2f}")
        print(f"Total: {total_pontos:.2f}")
        print("-" * 40)
        inscricao = int(input("Número de inscrição (9999 para encerrar): "))
    if total_pontos > maior_pontuacao:
        maior_pontuacao = total_pontos
        inscricao_vencedor = inscricao
    if maior_pontuacao != -1:
        print("\n" + "="*40)
        print(f"A EQUIPE VENCEDORA FOI A DE INSCRIÇÃO: {inscricao_vencedor}")
        print(f"PONTUAÇÃO TOTAL: {maior_pontuacao:.2f}")
        print("="*40)
main()