import numpy as np
from funcionalidades.interface import linha_horizontal

matriz = np.array([[6, 8, 2, 4, 10], [13, 1, 3, 7, 5]])

print('Matriz: ')
print(matriz)
linha_horizontal('*', 30)
print(f'Média: {np.mean(matriz):.2f}')
print(f'Mediana: {np.median(matriz):.2f}')
print(f'Desvio padrão: {np.std(matriz):.2f}')
print(f'Valor máximo: {np.max(matriz)}')
print(f'Valor mínimo: {np.min(matriz)}')
linha_horizontal('*', 30)