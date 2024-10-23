import time
def buscabinaria(lista, item):
    tempo = time.time()
    baixo = 0
    alto = len(lista) - 1
    iteracoes = 0
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        iteracoes += 1
        if chute == item:
            tempo = time.time() - tempo
            return meio, iteracoes, tempo
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1        
    tempo = time.time() - tempo
    return -1, iteracoes, tempo

import random
iteracoes = []
lista = []
lugar = []
tempo = []
tamanhoslista = [5, 10, 15, 20, 25]
for tamanho in tamanhoslista:
  lista.append(random.sample(range(50), tamanho))

for i in range(len(tamanhoslista)):
  lugarresul, iteracoesresul, temporesul = buscabinaria(lista[i], 20)
  iteracoes.append(iteracoesresul)
  lugar.append(lugarresul)
  tempo.append(temporesul)

print(tamanhoslista)
print(iteracoes)
print(lugar)
print(tempo)