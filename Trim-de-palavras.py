def main():
    texto = str(input("qual o texto: "))
    texto_revisado = str()
    for letra in texto:
        while letra in "abcdefghijklmnopqrstuvxwyz123456789":
            texto_revisado+= letra
    print(f"texto anterior {texto}")
    print(f"texto revisado {texto_revisado}")
main()