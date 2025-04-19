import numpy as np
from random import randint
from funcionalidades.interface import subtitulo

matriz = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
for i in range(5):
    for j in range(5):
        matriz[i][j] = randint(10, 99)

print('Matriz: ')
print(matriz)
subtitulo('Reshape', '*', 30)
print('Matriz (1X25):')
print(matriz.reshape(1, 25))
subtitulo('Flatten', '*', 30)
print(matriz.flatten())
subtitulo('Transpose', '*', 30)
print(matriz.transpose())
subtitulo('Números pares', '*', 30)
print(np.where(matriz % 2 == 0, matriz, 'ímpar'))
subtitulo('Estatísticas', '*', 30)
print(f'Média: {matriz.mean():.2f}')
print(f'Soma total: {matriz.sum()}')
print(f'Desvio padrão: {matriz.std():.2f}')
