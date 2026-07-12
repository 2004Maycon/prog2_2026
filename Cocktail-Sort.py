# Cocktail-Sort.py

def cocktail_sort(lista_produtos):

    n = len(lista_produtos)
    trocou = True
    inicio = 0
    fim = n - 1

    while trocou:
        trocou = False

    
        for i in range(inicio, fim):
            if lista_produtos[i][1].lower() > lista_produtos[i + 1][1].lower():
                lista_produtos[i], lista_produtos[i + 1] = lista_produtos[i + 1], lista_produtos[i]
                trocou = True

        
        for i in range(fim - 1, inicio - 1, -1):
            if lista_produtos[i][1].lower() > lista_produtos[i + 1][1].lower():
                lista_produtos[i], lista_produtos[i + 1] = lista_produtos[i + 1], lista_produtos[i]
                trocou = True

        inicio += 1


def main():
    lista_produtos = []

    with open("produtosTI.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = Server_line = linha.strip()
            
            # Transforma a linha em uma lista interna de atributos
            atributos = linha.split(",")
            atributos = [atrib.strip() for atrib in atributos]
            
            lista_produtos.append(atributos)

    cocktail_sort(lista_produtos)

    print(f"{'ID':<5} | {'Nome':<30} | {'Categoria':<15} | {'Marca':<12} | {'Preço':<10} | {'Garantia':<8} | {'Estoque':<8}")
    print("-" * 102)
    print()
    for p in lista_produtos:
        print(f"{p[0]:<5} | {p[1]:<30} | {p[2]:<15} | {p[3]:<12} | {p[4]:<10} | {p[5]:<8} | {p[6]:<8}")


if __name__ == "__main__":
    main()