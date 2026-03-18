def main():
    
    x = float(input("valor de x"))
    y = float(input("valor de y"))

    # 2. Calcula as bordas para ESSE valor de x
    borda_superior = 3 * x
    borda_inferior = x / 3

    # 3. Verifica se o y está no meio delas
    # Usamos abs(y) porque a questão pede |y|
    if abs(y) > borda_inferior and abs(y) < borda_superior:
        print("INTERIOR")
    else:
        print("EXTERIOR")
main()