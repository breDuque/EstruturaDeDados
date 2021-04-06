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
