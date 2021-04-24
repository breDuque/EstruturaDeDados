import random as r

def bubbleSort(array):
    n = len(array) - 1
    if (all(array[i] <= array[i+1] for i in range(len(array)-1))):
        return "Array ja esta ordenada!"
    else:
        for i in range(0, n):
            for j in range(n-1, i-1, -1):
                if array[j] > array[j+1]:
                    t = array[j]
                    array[j] = array[j+1]
                    array[j+1] = t
        return array


def RandomIntArray(lenght):
    n = []
    n = r.sample(range(0, 20000), lenght)

    return n


def SortedIntArray(lenght):
    a = []
    for i in range(0, lenght):
        a.append(i)

    return a


def InvertedIntArray(lenght):
    a = []
    a = SortedIntArray(lenght).copy()
    a.reverse()

    return a

print(bubbleSort(InvertedIntArray(100)))
print(bubbleSort(SortedIntArray(100)))
print(bubbleSort(RandomIntArray(100)))

def questao2(n):
    s = 0
    for i in range(0, n):
	    for j in range(0, n):
		    s = s + 1
    return s

def questao2(n):
    for i in range(0,n):
        i = 0 
        while i < n:
            i = i+1

def questao2(n):
    for j in range(0,n):  
        j = 0 
        while j < n:
            j = j+1


# def buscaSequencial(vetor, item):
#     pos = 0
#     encontrado = False

#     while pos < len(vetor) and not encontrado:
#         if vetor[pos] == item:
#             encontrado = True
#         else:
#             pos = pos+1

#     return encontrado

def buscaSequencial(vetor, item):
    for i in vetor:
        if i == item:
            return True
    
    return False

print(buscaSequencial(SortedIntArray(100), 55))
print(buscaSequencial(SortedIntArray(100), 155))

def insertionSort(vetor):
    n = len(vetor)
    for i in range(1, n):
        atual = vetor[i]
        j = i - 1
        while j >= 0 and atual < vetor[j]:
            vetor[j+1] = vetor[j]
            j -= 1
        vetor[j+1] = atual

    return vetor

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist=[20,30,40,90,50,60,70,80,100,110]

def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1

    return found
	
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))