def main():
    arq = open("texto.txt","rt", encoding= "utf8")
    texto = arq.read()
    arq.close()

    dicCHARS ={}
    for char in texto:
        if char in dicCHARS.keys():
            dicCHARS+= 1 
        else:
            dicCHARS[char]=1
        
    for  chave,valor in dicCHARS.items():
        print(f"{chave:4},{valor:4}")

main()