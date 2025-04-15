print('=' * 30)
print('Calculadora'.center(30))
print('=' * 30)
n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
print('=' * 30)
while True:
    opc = str(input('Escolha a operação [ + | - | x | / | % | ** ]: '))
    match opc:
        case '+':
            print(f'{n1} + {n2} = {n1 + n2}')
        case '-':
            print(f'{n1} - {n2} = {n1 - n2}')
        case 'x':
            print(f'{n1} x {n2} = {n1 * n2}')
        case '/':
            try:
                print(f'{n1} / {n2} = {n1 / n2}')
            except ZeroDivisionError:
                print('Não é possível fazer a divisão por zero!')
        case '%':
            try:
                print(f'{n1} % {n2} = {n1 % n2}')
            except ZeroDivisionError:
                print('Não é possível fazer o resto da divisão por zero!')
        case '**':
            print(f'{n1} ** {n2} = {n1 ** n2}')
        case _:
            print('Opção inválida!')
    while True:
        resp = str(input('Deseja fazer mais uma operação? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('===== Cálculos encerrados! ====')
