#633ns por loop
def soma(n):
    soma = 0
    for x in range(n+1):
        soma+= x

    return print(soma)

soma(10)

#116ns por loop
def soma2(n):
    return print((n * (n + 1)) / 2)

soma2(10)