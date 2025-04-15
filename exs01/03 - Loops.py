print('=' * 30)
print('Tabuada'.center(30))
print('=' * 30)
try:
    num = int(input('Digite um número inteiro: '))
except ValueError:
    print('Certifique-se de digitar um número inteiro!')
except KeyboardInterrupt:
    print('Programa interrompido!')
else:
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
finally:
    print('====Tabuada finalizada!====')
