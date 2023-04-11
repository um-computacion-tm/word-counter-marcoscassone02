
def contador_palabras(texto):
    Contador = texto.split()
    Resultado = {}  
    for i in Contador:
        if i not in Resultado:
            Resultado[i] = 1
        else:
            Resultado[i] += 1
    return Resultado


        
        
    
