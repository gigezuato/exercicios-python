import numpy as np
from funcionalidades.interface import subtitulo

temperaturas = np.array(np.random.uniform(15, 35, (7, 4)))
print('Temperaturas:')
print(np.round(temperaturas, 2))

subtitulo('Temperaturas Médias por cidades', '*', 30)
medias = np.mean(temperaturas, axis=0)
print(np.round(medias, 2))

subtitulo('Dias mais quentes', '*', 30)
temp_max = np.max(temperaturas)
dias_quente = np.where(temperaturas == temp_max)
for dia, cidade in zip(*dias_quente):
    print(f'- Dia: {dia + 1}, Cidade: {cidade + 1}')

subtitulo('Maior e menor temperatura', '*', 30)
temp_min = np.min(temperaturas)
for i in range(len(temperaturas)):
    for j in range(len(temperaturas[i])):
        if temperaturas[i][j] == temp_max:
            cidade_quente = j
        elif temperaturas[i][j] == temp_min:
            cidade_fria = j

print(f'Maior temperatura: {np.max(temperaturas):.2f} °C, Cidade: {cidade_quente}')
print(f'Menor temperatura: {np.min(temperaturas):.2f} °C, Codade: {cidade_fria}')