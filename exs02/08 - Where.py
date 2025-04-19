import numpy as np

matriz = np.array([[-2, 5, 8, -9, 3], [7, 10, -5, -1, -4]])
print('Matriz: ')
print(matriz)
print('Substituindo os negativos por zero: ')
nova_matriz = np.where(matriz < 0, 0, matriz)  # where(condição, valor se verdadeiro, valor se falso)
print(nova_matriz)