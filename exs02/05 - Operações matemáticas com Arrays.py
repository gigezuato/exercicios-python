import numpy as np
from funcionalidades.interface import linha_horizontal

matriz1 = np.array([[2, 6, 9], [7, 3, 4]])
matriz2 = np.array([[5, 1, 2], [4, 8, 6]])

print('Matriz 1:')
print(matriz1)
print('Matriz 2:')
print(matriz2)
linha_horizontal('*', 40)
print(f'matriz1 + matriz2 = {matriz1 + matriz2}')
print(f'matriz1 - matriz2 = {matriz1 - matriz2}')
print(f'matriz1 * matriz2 = {matriz1 * matriz2}')
print(f'matriz1 // matriz2 = {matriz1 // matriz2}')
linha_horizontal('*', 40)