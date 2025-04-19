import numpy as np
from funcionalidades.interface import subtitulo

matriz = np.array([[3, 9], [8, 1], [7, 9]])
subtitulo('Matriz', '*', 30)
print(matriz)
print('ÍNDICES:')
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f'Linha {i}, Coluna {j} - {matriz[i][j]}')

subtitulo('Tranposta', '*', 30)
matriz_transposta = matriz.transpose()
print(matriz_transposta)
for i in range(len(matriz_transposta)):
    for j in range(len(matriz_transposta[i])):
        print(f'Linha {i}, Coluna {j} - {matriz_transposta[i][j]}')