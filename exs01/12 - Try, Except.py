n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

try:
    div = n1 / n2
    print(f'{n1} / {n2} = {div:.2f}')
except ZeroDivisionError:
    print('Não é possível fazer a divisão por zero!')
