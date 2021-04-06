# %%



def soma(n):
    soma = 0
    for x in range(n+1):
        soma += x

    return soma


%timeit soma(10)

# %%


def soma2(n):
    return (n * (n + 1)) / 2


%timeit soma2(10)

# %%


def lista1():
    lista = []
    for i in range(1000):
        lista += [i]
    return lista


%timeit lista1()

# %%


def lista2():
    return range(1000)


%timeit lista2()


# %%
import matplotlib.pyplot as plt
import numpy as np
from math import log

n = np.linspace(1, 10, 100)

print(n)

labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential']
bigO = [np.ones(n.shape), np.log(n), n, n * np.log(n), n**2, n**3, 2**n]

plt.figure(figsize=(10,8))
plt.ylim(0,100)
for i in range(len((bigO))):
    plt.plot(n,bigO[i], label = labels[i])
plt.legend()
plt.xlabel('Runtime')
plt.xlabel('n')

# %%

lista = [1,2,3,4,5]

# Constant - O(1)
def constant(n):
    return n[0]

# Linear - O(n)
def linear(n):
    for i in n:
        print(i)

# Quadratic / Polynomial - O(n^2)
def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)
        print('---')


# Combination - O(1) + O(5) + O(n) + O(n) + O(3) -> O(9) + O(2n) -> O(n)
def combination(n):
    # O(1)
    print(n[0])
    
    # O(5)
    for i in range(5):
        print('teste', i)
    
    # O(n)
    for i in n:
        print(i)
    
    # O(n)
    for i in n:
        print(n)
    
    # O(3)
    print('Python')
    print('Python')
    print('Python')
# %%
