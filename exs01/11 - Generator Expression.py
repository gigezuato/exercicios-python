quadrados = (x ** 2 for x in range(1, 11))

for i, n in enumerate(quadrados):
    print(f'{i+1} ** 2 = {n}')