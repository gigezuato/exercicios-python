n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

try:
    div = n1 / n2
except ZeroDivisionError:
    print('Não é possível fazer a divisão por zero!')
else:
    print(f'{n1} / {n2} = {div:.2f}')
finally:
    print('Operação finalizada!')