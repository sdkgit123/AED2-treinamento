import random

lista = random.sample(range(0, 200), 10)
maior = 0

print(lista)

for i in range(len(lista)):
    if i == 0:
        maior = lista[i]
    elif lista[i] > maior:
        maior = lista[i]


print(maior)
