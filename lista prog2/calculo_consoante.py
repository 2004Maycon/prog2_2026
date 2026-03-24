def calcular_consoante(name):
    quant_cons = 0
    for i in range(len(name)):
         if name[i] not in "aeiouAEIOU":
              quant_cons+=1
    return quant_cons


def main():
    nome = str(input("qual o nome: "))
    lista_nome = []
    while nome != " ":
        lista_nome.append(nome)
        nome = str(input("qual o nome: cls"))
    print(f"essa é a lista {lista_nome}")
    if len(lista_nome) > 0 :
        for nome   in  lista_nome:
                consoante=calcular_consoante(nome)
                print(f'essa é o nome  {nome} a contidade {consoante}')
main()