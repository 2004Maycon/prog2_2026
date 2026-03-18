def main():
    r = 0
    denominador = 1
    sinal = 1
    termo= 4.0
    atual = termo/ denominador
    while atual >= 0.0001:
        r+= sinal*atual
        denominador+=2
        sinal*=-1
        atual = termo/ denominador
    print(f'Último termo verificado: {atual:.4f}')
    print(f"pi: {r:.5f}")
    print(f"denominador: {denominador}")
main()