def main():
    dicIN = {'ciência':
    [88,89,62,95],'linguagem':[77,78,84,80]}
    lstout = []
    lst_chaves = list(dicIN.keys())
    lst_chaves_a = lst_chaves[0]
    lst_chaves_b = lst_chaves [1]
    lsta=dicIN[lst_chaves_a]
    lstb = dicIN[lst_chaves_b]
    for i in range (len(dicIN[lst_chaves_b])):
        dic_aux = {lst_chaves_a:lsta[i],lst_chaves_b:lstb[i]}
        lstout.append(dic_aux)
    print(f"entrada:{dicIN}" )
    print(f"saida : {lstout}")

main()

