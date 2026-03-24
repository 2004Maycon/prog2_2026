def f_veiculo(a):
    linha = a.readline()
    print()
    print("TABELA VEICULO")
    print()
    while linha != "":
        print(linha,end="")
        linha =  a.readline()
        print("_"*90)
    a.close()
    return a
def f_proprietario(b):
    linha = b.readline()
    print()
    print("TABELA PROPRIETARIO")
    print()
    while linha != "":
        print(linha,end="")
        linha =  b.readline()
        print("_"*90)
    b.close()
    return b
def f_relatorio(lista1,lista2):
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            relat=open()
            relat.wite()
    return
def main():
    arq= open("tabveiculos.txt","rt",encoding="utf8")
    f_veiculo(arq)
    arq2= open("tabproprietario.txt","rt",encoding="utf8")
    f_proprietario(arq2)
    f_relatorio(arq,arq2)
main()
