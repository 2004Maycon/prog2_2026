
def shell_sort(lista_produtos):
  
    n = len(lista_produtos)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            pivo = lista_produtos[i]
            
            nome_pivo = pivo[1].lower() 
            j = i
            
            while j >= gap and lista_produtos[j - gap][1].lower() > nome_pivo:
                lista_produtos[j] = lista_produtos[j - gap]
                j -= gap
                
            lista_produtos[j] = pivo
        gap //= 2




def main():
    
    lista_produtos = []
    
    
    with open("produtosTI.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            
           
            atributos = linha.split(",")
            atributos = [atrib.strip() for atrib in atributos]
            
            lista_produtos.append(atributos)

   
    shell_sort(lista_produtos)

    
    print(f"{'ID':<5} | {'Nome':<30} | {'Categoria':<15} | {'Marca':<12} | {'Preço':<10} | {'Garantia':<8} | {'Estoque':<8}")
    print("-" * 102)
    for p in lista_produtos:
        print(f"{p[0]:<5} | {p[1]:<30} | {p[2]:<15} | {p[3]:<12} | {p[4]:<10} | {p[5]:<8} | {p[6]:<8}")





if __name__ == "__main__":
    main()