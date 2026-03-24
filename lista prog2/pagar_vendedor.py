def main():
    
    quantidade_recebeu_comissao=[]
    valor_recebido =200
    valor_venda = float(input("qual valor de venda: "))
    for i in range(1):
        comisao = (valor_venda*(9/100))+valor_recebido
        quantidade_recebeu_comissao.append(comisao)
    print(quantidade_recebeu_comissao)
main()