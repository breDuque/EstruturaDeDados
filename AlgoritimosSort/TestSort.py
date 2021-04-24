import random as r
import time as t

loopExtMergeSort = 0
loopIntMergeSort = 0
loopExtHeapSort = 0
loopIntHeapSort = 0
loopExtQuickSort = 0
loopIntQuickSort = 0


def testAllMethods(methodList, arrayLength, arrayType):
    antesExterno = t.time()
    array = arrayType(arrayLength)
    print("\n----------------------------------------------------------------------")
    print("Rodando testes com uma array do tipo {} com {} elementos\n".format(
        arrayType.__name__, arrayLength))

    for method in methodList:
        print("--------------------------------")
        print(method.__name__)

        antesInterno = t.time()

        if method == quickSort:
            global loopIntQuickSort
            global loopExtQuickSort
            print("* Devido ao quicksort exceder o limite de recursão com 1000 elementos,\n  todos os testes foram feitos usando arrays com 997 elementos")
            quickSortArray = arrayType(997)
            n = len(quickSortArray)
            method(quickSortArray.copy(), 0, n-1)
            print("Externo: {}".format(loopExtQuickSort),"\nInterno: {}".format(loopIntQuickSort))
            loopIntQuickSort, loopExtQuickSort = 0, 0
        elif method == heapSort:
            global loopExtHeapSort
            global loopIntHeapSort
            method(array.copy())
            print("Externo: {}".format(loopExtHeapSort),"\nInterno: {}".format(loopIntHeapSort))
            loopExtHeapSort, loopIntHeapSort = 0, 0
        elif method == mergeSort:
            global loopExtMergeSort
            global loopIntMergeSort
            method(array.copy())
            print("Externo: {}".format(loopExtMergeSort),"\nInterno: {}".format(loopIntMergeSort))
            loopExtMergeSort, loopIntMergeSort = 0, 0
        else:
            print("{}\n{}".format(method(array.copy())[0], method(array.copy())[1]))

        depoisInterno = t.time()
        total = (depoisInterno-antesInterno)*1000
        print("Tempo decorrido: {:0.2f}ms".format(total))
        print("\n")

    depoisExterno = t.time()
    totalExterno = (depoisExterno - antesExterno)*1000
    print("----------------Tempo decorrido no total: {:0.2f}ms----------------\n".format(totalExterno))

# region Array Types

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

#endregion

# region Algoritimos

def bubbleSort(vetor):
    n = len(vetor)
    loopIntQUickSorterno = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            loopIntQUickSorterno += 1
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

    return ("Externo: {}".format(i), "Interno: {}".format(loopIntQUickSorterno))


def selectionSort(vetor):
    n = len(vetor)
    loopIntQUickSorterno = 0

    for i in range(n):
        id_minimo = i
        for j in range(i + 1, n):
            loopIntQUickSorterno += 1
            if vetor[id_minimo] > vetor[j]:
                id_minimo = j

        temp = vetor[i]
        vetor[i] = vetor[id_minimo]
        vetor[id_minimo] = temp

    return ("Externo: {}".format(i), "Interno: {}".format(loopIntQUickSorterno))


def insertionSort(vetor):
    n = len(vetor)
    loopIntQUickSorterno = 0
    loopExterno = 0

    for i in range(1, n):
        loopExterno += 1
        atual = vetor[i]
        j = i - 1
        while j >= 0 and atual < vetor[j]:
            loopIntQUickSorterno += 1
            vetor[j+1] = vetor[j]
            j -= 1
        vetor[j+1] = atual

    return ("Externo: {}".format(loopExterno), "Interno: {}".format(loopIntQUickSorterno))


def shellSort(vetor):
    n = len(vetor)
    intervalo = 1
    loopIntQUickSorterno = 0
    loopExterno = 0

    while intervalo < n:
        intervalo = intervalo * 3 + 1
    while intervalo > 1:
        intervalo //= 3
        for i in range(intervalo, n, intervalo):
            loopExterno += 1
            temp = vetor[i]
            j = i - intervalo
            while j >= 0 and temp < vetor[j]:
                loopIntQUickSorterno += 1
                vetor[j+intervalo] = vetor[j]
                j -= intervalo
            vetor[j+intervalo] = temp

    return ("Externo: {}".format(loopExterno), "Interno: {}".format(loopIntQUickSorterno))


def mergeSort(vetor):
    global loopExtMergeSort
    global loopIntMergeSort
    loopExtMergeSort += 1
    if len(vetor) > 1:
        divisao = len(vetor)//2
        esquerda = vetor[:divisao].copy()
        direita = vetor[divisao:].copy()

        mergeSort(esquerda)
        mergeSort(direita)

        i = j = k = 0

        # Ordena esquerda e direita
        while i < len(esquerda) and j < len(direita):
            loopIntMergeSort += 1
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1

        # Ordenação final
        while i < len(esquerda):
            loopIntMergeSort += 1
            vetor[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            loopIntMergeSort += 1
            vetor[k] = direita[j]
            j += 1
            k += 1


def heapSort(vetor):
    n = len(vetor)
    global loopExtHeapSort

    for i in range(n // 2 - 1, -1, -1):
        loopExtHeapSort += 1
        heapify(vetor, n, i)

    for i in range(n-1, 0, -1):
        loopExtHeapSort += 1
        vetor[i], vetor[0] = vetor[0], vetor[i]   # swap
        heapify(vetor, i, 0)


def heapify(vetor, n, i):
    global loopIntHeapSort
    loopIntHeapSort += 1

    maior = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and vetor[i] < vetor[l]:
        maior = l

    if r < n and vetor[maior] < vetor[r]:
        maior = r

    if maior != i:
        vetor[i], vetor[maior] = vetor[maior], vetor[i]

        heapify(vetor, n, maior)


def quickSort(vetor, min, max):
    global loopExtQuickSort
    loopExtQuickSort += 1
    if len(vetor) == 1:
        return vetor
    if min < max:

        pivotIndex = quickSortPartition(vetor, min, max)

        quickSort(vetor, min, pivotIndex - 1)
        quickSort(vetor, pivotIndex + 1, max)


def quickSortPartition(vetor, min, max):
    i = (min-1)
    pivot = vetor[max]

    for j in range(min, max):
        global loopIntQuickSort
        loopIntQuickSort += 1
        if vetor[j] <= pivot:

            i = i+1
            vetor[i], vetor[j] = vetor[j], vetor[i]

    vetor[i+1], vetor[max] = vetor[max], vetor[i+1]
    return (i+1)

# endregion


methodList = [bubbleSort, selectionSort, insertionSort,
              shellSort, mergeSort, heapSort, quickSort]

testAllMethods(methodList, 1000, SortedIntArray)
testAllMethods(methodList, 1000, InvertedIntArray)
testAllMethods(methodList, 1000, RandomIntArray)
testAllMethods(methodList, 1000, RandomIntArray)
testAllMethods(methodList, 1000, RandomIntArray)

testAllMethods(methodList, 10000, SortedIntArray)
testAllMethods(methodList, 10000, InvertedIntArray)
testAllMethods(methodList, 10000, RandomIntArray)
testAllMethods(methodList, 10000, RandomIntArray)
testAllMethods(methodList, 10000, RandomIntArray)