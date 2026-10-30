import random

any_numbers = random.sample(range(1, 12), 10) # 10 Numbers --
lists = [2, 5, 7, 4, 10, 2, 6, 7]
size = len(lists)

def Bubble_Sort(lista):
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    return lista

print(Bubble_Sort(lists))
