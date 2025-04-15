try:
    num = int(input('Digite um número inteiro: '))
except ValueError:
    print('Certifique-se de digitar um número inteiro!')
else:
    if num % 2 == 0:
        print(f'O número {num} é PAR')
    else:
        print(f'O número {num} é ÍMPAR')
    if num > 0:
        print(f'{num} é POSITIVO')
    elif num < 0:
        print(f'{num} é NEGATIVO')
    else:
        print('O número digitado é o ZERO')
