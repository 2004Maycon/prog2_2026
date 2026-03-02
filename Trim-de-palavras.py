def main():
    texto = str(input("qual o texto: "))
    texto_revisado = str()
    nada = str()
    for letra in texto:
        if letra in "," or letra in "." or  letra in "/" or  letra in "()" or  letra in "-" or  letra in "_" or  letra in "=" or  letra in "!" or  letra in ":" or  letra in ";" or  letra in "?":
            nada+= letra
        else:
            texto_revisado+= letra
    print(f"texto anterior {texto}")
    print(f"texto revisado {texto_revisado}")
    print(nada)
main()