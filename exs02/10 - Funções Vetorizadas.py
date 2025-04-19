import numpy as np


def funcao(x):
    return x ** 2 + 2 * x + 1


funcao_vetorizada = np.vectorize(funcao)
matriz = np.array([[8, 6, 2], [3, 4, 5]])
print('Matriz: ')
print(matriz)
print('Matriz depois da função: ')
print(funcao_vetorizada(matriz))