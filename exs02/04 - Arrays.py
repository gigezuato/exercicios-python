import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(f'Array original: {matriz}')
print(f'Matriz achatada: {matriz.flatten()}')
print(f'Matriz (3X2): {matriz.reshape((3, 2))}')