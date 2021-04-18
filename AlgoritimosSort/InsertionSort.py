import random as r

def insertionSort(x):
        n = len(x)
        for i in range(1, n):
            atual = x[i]
            j = i - 1
            while j >= 0 and atual < x[j]:
                x[j+1] = x[j]
                j = j - 1
            x[j+1] = atual
        return x
    
print(insertionSort([38, 27, 43, 3, 9, 82, 10]))

def GenerateRandomIntArray():   
    n = []
    n = r.sample(range(0,100000),1000)
    return n

print(GenerateRandomIntArray())