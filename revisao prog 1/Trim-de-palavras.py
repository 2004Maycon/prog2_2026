def main():
    inicio = 0 
    texto = str(input("qual o texto: "))
    texto_revisado = str()
    nada = str()
    while inicio <len(texto)and not texto[inicio].isalnum():
        inicio+=1
    fim=len(texto)-1
    while fim > inicio and not (texto[fim].isalnum()):
        fim -= 1
    texto_revisado = texto[inicio : fim + 1]
    print(f"texto anterior {texto}")
    print(f"texto revisado {texto_revisado}")
main()