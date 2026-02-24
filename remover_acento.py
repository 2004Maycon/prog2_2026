def remov_acento(t):
    alterador = str()
    for i in range(len(t)):
        if t[i] == 'á' or t[i] == 'á' or  t[i] == 'á' or t[i] == 'â' or t[i] == 'ã':
            alterador+="a"
        elif t[i] == 'é' or t[i] == 'è' or  t[i] == 'ê':
            alterador+="e"
        elif t[i] == 'í' or t[i] == 'ì' or  t[i] == 'î':
            alterador+="i"
        elif t[i] == 'ó' or t[i] == 'ò' or  t[i] == 'ô' or  t[i] == 'õ' :
            alterador+="o"
        elif t[i] == 'ú' or t[i] == 'ù' or  t[i] == 'û':
            alterador+="u"
        else:
            alterador+=t[i]
    return alterador

def main():
    text="coração exemplo caracteristica tostões"
    texto_sa = remov_acento(text)
    print(f"antes:{text}")
    print(f"depois: {texto_sa}")
    
main()