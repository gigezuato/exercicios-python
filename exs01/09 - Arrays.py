from array import array

inteiros = array('i', [])
soma = 0

for i in range(0, 5):
    n = int(input(f'Digite o {i+1}° valor inteiro:'))
    inteiros.append(n)

maior = max(inteiros)
menor = min(inteiros)
soma = sum(inteiros)
media = soma / len(inteiros)
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
print(f'Média dos valores: {media:.2f}')