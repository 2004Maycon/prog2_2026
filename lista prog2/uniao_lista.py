#Construa uma função para calcular a intersecção de dois conjuntos representados por duas
#listas passadas como parametros da função. A lista intersecção deve ser o valor retornado pela
#função. Construa um programa principal para testar a sua função.

def main():
    intercessao=[]
    listaA= [input("lista A: ")]
    listaB= [input("lista B: ")]
    for listaB in  listaA:
        intercessao.append(listaB)  
    print("-"*20)
    print(f"essa é a intecessão{intercessao}")
    print("-"*20)
    print(f"conjuntoA{listaA}")
    print("-"*20)
    print(f"conjuntoB{listaB}")
main()