nomes = []

for i in range(10):
    nomes.append(str(input(f'Digite o {i + 1}° nome: ')).strip().title())

print(f'Em ordem alfabpetica: {sorted(nomes)}')

nomes_vogais = list([nome for nome in nomes if nome[0] in 'AEIOU'])
print(f'Nomes que começam com vogal: {nomes_vogais}')
nomes_mais5 = list([nome for nome in nomes if len(nome) > 5])
print(f'Nomes com mais de 5 letras: {nomes_mais5}')
print(f'Lista inversa: {nomes[9:: -1]}')
maiusculo = list([nome.upper() for nome in nomes])
print(f'Nomes em maiúsculo: {maiusculo}')