import random as r
import time as t

def GenerateRandomIntArray(lenght):   
    n = []
    n = r.sample(range(0,20000),lenght)
    return n

def bubbleSort(vetor):
    n = len(vetor)
    jCounter = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            jCounter += 1
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

    return ("Externo {}".format(i), "Interno {}".format(jCounter))

antes = t.time()
print(bubbleSort(GenerateRandomIntArray(1000)))
depois = t.time()
total = (depois-antes)*1000
print(total)