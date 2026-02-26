def main():
    palavra= str(input("digite sua palavra: "))
    palavra_aux= str()
    for letra in palavra[::-1]:
        palavra_aux+=letra
    if palavra == palavra_aux:
        print("É um palíndromo!")
    else:
        print(" Não é um palíndromo!")
main()
