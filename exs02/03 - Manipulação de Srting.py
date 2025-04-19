frase = str(input('Digite uma frase: ')).strip()
lista_palavras = frase.split()

print(f'Essa frase tem {len(lista_palavras)} palavras.')
print(f'Frase em maiúscula: {frase.upper()}')
print(f'Frase invertida: {frase[::-1]}')
if frase.count('Python') or frase.count('python') > 0:
    print('A frase tem a palavra python!')
else:
    print('A frase não tem a palavra python!')