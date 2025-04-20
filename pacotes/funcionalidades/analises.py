import numpy as np
from funcionalidades.interface import subtitulo


def array_idade(dados):
    lista_idades = []
    for i in range(len(dados)):
        lista_idades.append(dados[i]['Idade'])
    idades = np.array(lista_idades)
    return idades


def set_cidade(dados):
    lista_cidades = []
    for i in range(len(dados)):
        lista_cidades.append(dados[i]['Cidade'])
    cidades = set(lista_cidades)
    return cidades


def analise_idades(idades):
    media = np.round(np.mean(idades))
    maiores_idade = len(np.where(idades >= 18)[0])
    menores_idade = len(np.where(idades < 18)[0])
    subtitulo('Análise de idades', '*', 25)
    print(f'Média das idades: {media}')
    print(f'Quantidade de usuários maiores de idade: {maiores_idade}')
    print(f'Quantidade de usuários menores de idade: {menores_idade}')


def analise_cidades(cidades):
    subtitulo('Analise de cidades', '*', 25)
