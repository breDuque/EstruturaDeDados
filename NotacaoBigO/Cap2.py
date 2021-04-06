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