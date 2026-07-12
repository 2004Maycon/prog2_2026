

def main():
    # Uso estrito de open, readline e close conforme as regras da prova
    arquivo = open("documento.txt", "r", encoding="utf-8")
    texto_original = ""
    linha = arquivo.readline()
   
    mapa_acentos = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a', 'ä': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
        'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o', 'ö': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
        'ç': 'c',
        'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A', 'Ä': 'A',
        'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
        'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
        'Ó': 'O', 'Ò': 'O', 'Õ': 'O', 'Ô': 'O', 'Ö': 'O',
        'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U',
        'Ç': 'C'
    }

    while linha != "":
        texto_original = texto_original + linha
        linha = arquivo.readline()
    texto_limpo = ""

    for caractere in texto_original:
        if caractere in mapa_acentos:
            texto_limpo += mapa_acentos[caractere]
        else:
            texto_limpo += caractere
    
 
    
        
    arquivo.close()
    
    
    print("--- Texto Original ---")
    print(texto_original)
    print("\n--- Texto Sem Acentos ---")
    print(texto_limpo)

# Invocação da função principal
main()