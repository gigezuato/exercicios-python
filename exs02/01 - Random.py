from random import randint, shuffle, choice, sample

numeros = []
for i in range(15):
    numeros.append(randint(1, 100))

print(f'Os números sorteados foram: {numeros}')
print(f'O menor valor da lista é: {min(numeros)}')
print(f'O maior valor da lista é: {max(numeros)}')
shuffle(numeros)
print(f'Lista embaralhada: {numeros}')
print(f'Número aleatório escolhido: {choice(numeros)}')
print(f'Nova amostra: {sample(numeros, 5)}')