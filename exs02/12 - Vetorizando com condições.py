import numpy as np
from random import randint
from funcionalidades.interface import subtitulo

matriz = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

for i in range(3):
    for j in range(5):
        matriz[i][j] = randint(-20, 20)
print('Matriz:')
print(matriz)


def classifica(x):
    if x > 0:
        return 'Positivo'
    elif x < 0:
        return 'Negativo'
    else:
        return 'Zero'


subtitulo('Aplicando a função vetorizada', '*', 30)
classifica_vetorizada = np.vectorize(classifica)
matriz_classificada = classifica_vetorizada(matriz)
print(matriz_classificada)

subtitulo('Contagem', '*', 30)
positivo = negativo = zero = 0
for i in range(3):
    for j in range(5):
        if matriz_classificada[i][j] == 'Positivo':
            positivo += 1
        elif matriz_classificada[i][j] == 'Negativo':
            negativo += 1
        else:
            zero += 1
print(f'Positivos: {positivo}')
print(f'Negativos: {negativo}')
print(f'Zero: {zero}')

# Versão menor
'''
import numpy as np
from random import randint
from funcionalidades.interface import subtitulo

matriz = np.array([[randint(-20, 20) for _ in range(5)] for _ in range(3)])
print('Matriz:')
print(matriz)


def classifica(x):
    return 'Positivo' if x > 0 else 'Negativo' if x < 0 else 'Zero'


subtitulo('Aplicando a função vetorizada', '*', 30)
matriz_classificada = np.vectorize(classifica)(matriz)
print(matriz_classificada)

subtitulo('Contagem', '*', 30)
positivo = sum(1 for linha in matriz_classificada for valor in linha if valor == 'Positivo')
negativo = sum(1 for linha in matriz_classificada for valor in linha if valor == 'Negativo')
zero = sum(1 for linha in matriz_classificada for valor in linha if valor == 'Zero')

print(f'Positivos: {positivo}')
print(f'Negativos: {negativo}')
print(f'Zero: {zero}')
'''