import numpy as np
from funcionalidades.interface import subtitulo

matriz1 = np.array([[5, 8, 9], [3, 6, 4]])
matriz2 = np.array([8, 1, 2])

subtitulo('Matrizes', '*', 30)
print('Matriz 1: ')
print(matriz1)
print('Matriz 2: ')
print(matriz2)

subtitulo('Soma com Broadcasting', '*', 30)
print(f'matriz1 + matriz2 = {matriz1 + matriz2}')

subtitulo('Explicando', '*', 30)
print('''
    Como as matrizes possuem formatos diferentes - matriz1 = 2X3 e matriz2 = 1X3 -
    o mecanismo de Broadcasting expande a matriz menor para que a soma seja possível.
    Assim, a matriz1 continua normal e a matriz2 expande para [[8 1 2] [8 1 2]].
''')