from random import choice, shuffle, sample
from time import sleep

lista_nomes = []
while True:
    nome = str(input('Digite um nome (quando quiser parar, digite sair): ')).strip().title()
    if nome == 'Sair':
        print('Saindo...')
        sleep(1)
        break
    else:
        lista_nomes.append(nome)

print(f'Foram inseridos {len(lista_nomes)} nomes.')
print(f'Aqui está a lista original: {lista_nomes}')
print(f'Lista em ordem alfabética: {sorted(lista_nomes)}')
print(f'O nome escolhido foi: {choice(lista_nomes)}')
shuffle(lista_nomes)
print(f'Após embaralhar a lista, o novo resultado do sorteio é: {choice(lista_nomes)}')
if len(lista_nomes) >= 3:
    print(f'Amostra com três nomes escolhidos: {sample(lista_nomes, 3)}')