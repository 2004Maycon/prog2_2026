def calculo_ponto(a,b):
    D = abs(a - b)
    if D < 3:
        return 100.0
    elif  (D >= 3) and (D <= 5):
        return 80.0
    else:
        return  80.0 - (D - 5) / 5
def main():
    maior_pontuacao = -1.0
    inscricao_vencedor = 0
    tempo1 = float(input(f"Digite o tempo-padrão da etapa : "))
    tempo2 = float(input(f"Digite o tempo-padrão da etapa : "))
    tempo3 = float(input(f"Digite o tempo-padrão da etapa : "))

    inscricao = int(input("Número de inscrição (9999 para encerrar): "))
    while inscricao != 9999:
        t_e1 = float(input(f"Digite o tempo da equipe na etapa : "))
        t_e2 = float(input(f"Digite o tempo da equipe na etapa : "))
        t_e3 = float(input(f"Digite o tempo da equipe na etapa : "))
        ponto1= calculo_ponto(tempo1,t_e1)
        ponto2=calculo_ponto(tempo2,t_e2)
        ponto3=calculo_ponto(tempo3,t_e3)
        total_pontos = ponto1 + ponto2 + ponto3
        
        print(f"Equipe: {inscricao}")
        print(f"Pontos Etapa 1: {t_e1:.2f} | Etapa 2: {t_e2:.2f} | Etapa 3: {t_e3:.2f}")
        print(f"Total: {total_pontos:.2f}")
        print("-" * 40)
       
        if total_pontos > maior_pontuacao:
            maior_pontuacao = total_pontos
            inscricao_vencedor = inscricao
        inscricao = int(input("Número de inscrição (9999 para encerrar): "))

    if maior_pontuacao != -1:
        print("\n" + "="*40)
        print(f"A EQUIPE VENCEDORA FOI A DE INSCRIÇÃO: {inscricao_vencedor}")
        print(f"PONTUAÇÃO TOTAL: {maior_pontuacao:.2f}")
        print("="*40)
main()