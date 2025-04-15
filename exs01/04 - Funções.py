def verifica_primo(n):
    div = 0
    for i in range(1, n+1):
        if n % i == 0:
            div += 1

    if div == 2:
        return True


num = int(input('Digite um número inteiro: '))
if verifica_primo(num):
    print(f'O número {num} é PRIMO!')
else:
    print(f'O número {num} NÃO é primo!')
