import numpy as np
from funcionalidades.interface import subtitulo

temperaturas = np.array(np.random.uniform(15, 35, 28))
temperaturas_forma = np.round(temperaturas.reshape((4, 7)), 1)
print('Temperaturas:')
print(np.round(temperaturas_forma, 1))

subtitulo('Temperaturas Médias por cidades', '*', 30)
for i in range(4):
    media = np.mean(temperaturas_forma[i])
    print(f'Temperatura média da cidade {i + 1}: {np.round(media, 1)} °C')

subtitulo('Dias mais quentes', '*', 30)
for i in range(4):
    dias_quente = np.where(temperaturas_forma[i] == np.max(temperaturas_forma[i]))
    print(f'Cidade {i + 1}: Dia {dias_quente[0][0] + 1}')

subtitulo('Maior e menor temperatura', '*', 30)
temp_max = np.round(np.max(temperaturas_forma), 1)
temp_min = np.round(np.min(temperaturas_forma), 1)

for cidade in range(4):
    for temp in range(7):
        if temperaturas_forma[cidade][temp] == temp_max:
            print(f'Maior temperatura: {temp_max} °C, Cidade: {cidade + 1}')
        elif temperaturas_forma[cidade][temp] == temp_min:
            print(f'Menor temperatura: {temp_min} °C, Cidade: {cidade + 1}')