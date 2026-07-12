def bd2dic(nomearq):
    dicionario_veiculos = {}
    
    with open(nomearq, 'r', encoding='utf-8') as arquivo:
        linhas = [linha.strip() for linha in arquivo if linha.strip()]
        
        for i in range(0, len(linhas), 4):
            if i + 3 < len(linhas):
                placa = linhas[i]
                modelo = linhas[i+1]
                marca = linhas[i+2].lower()  
                km = linhas[i+3]
                    
                dicionario_veiculos[placa] = {
                    "modelo": modelo,
                    "marca": marca,
                    "km": km
                }
   
    return dicionario_veiculos


def dic2marcas(dic):
    dicionario_marcas = {}
    
    for placa, dados in dic.items():
        marca = dados["marca"]
        
        veiculo = {
            "placa": placa,
            "modelo": dados["modelo"],
            "marca": marca,
            "km": dados["km"]
        }
        
        if marca not in dicionario_marcas:
            dicionario_marcas[marca] = []
            
        dicionario_marcas[marca].append(veiculo)
        
    return dicionario_marcas


def dic2files(dic2):
    for marca, lista_veiculos in dic2.items():
        nome_arquivo = f"{marca}.txt"
        
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            for veiculo in lista_veiculos:
                linha = f"{veiculo['placa']}, {veiculo['modelo']}, {veiculo['marca']}, {veiculo['km']}\n"
                arquivo.write(linha)


def main():
    arquivo_entrada = "bdveiculos.txt"
    
    dados_veiculos = bd2dic(arquivo_entrada)
    
    if dados_veiculos:
        dados_por_marca = dic2marcas(dados_veiculos)
        
        dic2files(dados_por_marca)


if __name__ == "__main__":
    main()