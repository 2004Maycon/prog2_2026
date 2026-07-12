def filtrar_estudantes(dicionario_entrada):
    dicionario_saida = {}
    
    
    for nome in dicionario_entrada:
        dados = dicionario_entrada[nome]
        altura = dados[0]
        peso = dados[1]
        
        
        if altura > 1.75 and peso > 70:
            dicionario_saida[nome] = dados
            
    return dicionario_saida

def main():
    
    dados_estudantes = {
        'César': (1.77, 72), 
        'Aldo': (1.67, 65), 
        'Maria': (1.65, 68), 
        'Pedro': (1.72, 66)
    }
    
    
    resultado = filtrar_estudantes(dados_estudantes)
    
    
    print(resultado)


main()