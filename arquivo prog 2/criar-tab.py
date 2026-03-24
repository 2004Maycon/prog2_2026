def main():
    arq= open("tabproprietario.txt","rt",encoding="utf8")
    linha = arq.readline()
    while linha != "":
        print(linha,end="")
        linha =  arq.readline()
    arq.close()
main()