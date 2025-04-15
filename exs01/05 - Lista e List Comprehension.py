lista = []

for i in range(0, 5):
    lista.append(int(input(f'Digite o {i+1} valor: ')))

pares = [n for n in lista if n % 2 == 0]

print(f'A lista completa é: {lista}')
print(f'Lista de números pares: {pares}')
print(f'A soma de todos os valores na lista é: {sum(lista)}')