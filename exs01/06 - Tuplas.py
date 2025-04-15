cores = ('vermelho', 'azul', 'verde', 'amarelo')

try:
    ind = int(input('Digite o número do índice: '))
    print(f'A cor correspondente ao índice digitado é {cores[ind]}')
except IndexError:
    print('índice inválido!')
except ValueError:
    print('O valor do índice é um número inteiro!')
finally:
    print('Programa encerrado!')