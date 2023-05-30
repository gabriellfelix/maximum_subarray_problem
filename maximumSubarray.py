import sys

def maximumSubarray(vetor):

    somaMaximaElemento = vetor.copy()

    pos = len(somaMaximaElemento) - 2

    somaMaxima = somaMaximaElemento[pos+1]
    posSomaMaxima = pos+1
    
    while(pos>=0):
        if ((somaMaximaElemento[pos+1] + somaMaximaElemento[pos]) > somaMaximaElemento[pos]):
            
            somaMaximaElemento[pos] = (somaMaximaElemento[pos+1] + somaMaximaElemento[pos])

        if (somaMaxima < somaMaximaElemento[pos]):
            somaMaxima = somaMaximaElemento[pos]
            posSomaMaxima = pos

        pos -= 1

    
    elementosSomaMaxima = []
    somaParcial = sys.float_info.min

    while (somaParcial != somaMaxima):
        if (somaParcial == sys.float_info.min):
            somaParcial = vetor[posSomaMaxima]

        else:
            somaParcial += vetor[posSomaMaxima]
            
        elementosSomaMaxima.append(vetor[posSomaMaxima])

        posSomaMaxima += 1
    

    return somaMaxima, elementosSomaMaxima

